import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

from db_fxns import *
import streamlit.components.v1 as stc
HTML_BANNER = """
    <div style="background-color:#464e5f;padding:10px;border-radius:10px">
    <h1 style="color:white;text-align:center;">ToDo App (CRUD)</h1>
    <p style="color:white;text-align:center;">Built with Streamlit</p>
    </div>
    """
def main():
    st.title("To do App with Streamlit")
    menu = ["Create","Read","Update","Delete","About"]
    choice= st.sidebar.selectbox("Menu", menu)

    create_table()
    if choice =="Create":
        st.subheader("Add Items")
        # Layout
        col1,col2 =st.columns(2)
        with col1:
            task =st.text_area("Task to Do ")
        with col2:
            task_status=st.selectbox("Status",["ToDo","Doing"])
            task_due_date= st.date_input("Due Date")
        if st.button("Add Task"):
            add_data(task,task_status,task_due_date)
            st.success("Successfully added Data:{}".format(task))


    elif choice=="Read":
        st.subheader("View Items")
        result=view_all_data()
        #st.write(result)
        with st.expander("View All Data"):
            df = pd.DataFrame(result,columns=['Task','Status','Due Date'])
            st.dataframe(df)
        with st.expander ("Task Status"):
            task_df =df['Status'].value_counts().to_frame()
            st.dataframe(task_df)
        with st.expander ("Task Status2"):
            task_df2 =df['Status'].value_counts().to_frame()
            task_df2 =task_df2.reset_index()
            st.dataframe(task_df2)
            p1=px.pie(task_df2, names='index',values='Status')
            st.plotly_chart(p1,use_container_width=True)

    elif choice =="Update":
        st.subheader("Edit/Update Items")
        result = view_all_data()
        with st.expander("Current Data"):
            df = pd.DataFrame(result, columns=['Task', 'Status', 'Due Date'])
            st.dataframe(df)
        list_of_tasks = [i[0] for i in view_all_task_names()]
        selected_task = st.selectbox("Task", list_of_tasks)
        task_result = get_task(selected_task)
        st.write(task_result)

        if task_result:
            task = task_result[0][0]
            task_status = task_result[0][1]
            task_due_date = task_result[0][2]

            col1, col2 = st.columns(2)

            with col1:
                new_task = st.text_area("Task To Do", task)

            with col2:
                new_task_status = st.selectbox(task_status, ["ToDo", "Doing", "Done"])
                new_task_due_date = st.date_input(task_due_date)

            if st.button("Update Task"):
                edit_task_data(new_task, new_task_status, new_task_due_date, task, task_status, task_due_date)
                st.success("Updated ::{} ::To {}".format(task, new_task))

            with st.expander("View Updated Data"):
                result = view_all_data()
                # st.write(result)
                clean_df = pd.DataFrame(result, columns=["Task", "Status", "Date"])
                st.dataframe(clean_df)



    elif choice=="Delete":
        st.subheader("Delete Item")
        with st.expander("View Data"):
            result = view_all_data()
            # st.write(result)
            clean_df = pd.DataFrame(result, columns=["Task", "Status", "Date"])
            st.dataframe(clean_df)

        unique_list = [i[0] for i in view_all_task_names()]
        delete_by_task_name = st.selectbox("Select Task", unique_list)
        if st.button("Delete"):
            delete_data(delete_by_task_name)
            st.warning("Deleted: '{}'".format(delete_by_task_name))

        with st.expander("Updated Data"):
            result = view_all_data()
            # st.write(result)
            clean_df = pd.DataFrame(result, columns=["Task", "Status", "Date"])
            st.dataframe(clean_df)

    else:
        st.subheader("About")
        st.write("Andrey Boyarchuk Training Exercise")





if __name__ == '__main__':
    main()