import streamlit as st
from pathlib import Path

st.title("📁 File Handling App")
st.write("Create, read, update, and delete files")

# Choose an operation
operation = st.selectbox(
    "Choose an operation",
    ["Create File", "Read File", "Update File", "Delete File"]
)

# ---------------- CREATE FILE ----------------
if operation == "Create File":

    filename = st.text_input("Enter file name")

    content = st.text_area("Enter file content")

    if st.button("Create File"):

        if filename:
            path = Path(filename)

            if not path.exists():
                with open(path, "w") as file:
                    file.write(content)

                st.success("File created successfully!")

            else:
                st.error("File already exists!")

        else:
            st.warning("Please enter a file name.")


# ---------------- READ FILE ----------------
elif operation == "Read File":

    filename = st.text_input("Enter file name")

    if st.button("Read File"):

        path = Path(filename)

        if path.exists():

            with open(path, "r") as file:
                content = file.read()

            st.text_area("File Content", content, height=200)

        else:
            st.error("File does not exist!")


# ---------------- UPDATE FILE ----------------
elif operation == "Update File":

    filename = st.text_input("Enter file name")

    update_type = st.selectbox(
        "Choose update operation",
        ["Rename File", "Append Content", "Overwrite Content"]
    )

    if update_type == "Rename File":

        new_name = st.text_input("Enter new file name")

        if st.button("Rename"):

            path = Path(filename)
            new_path = Path(new_name)

            if path.exists():

                if not new_path.exists():
                    path.rename(new_path)
                    st.success("File renamed successfully!")

                else:
                    st.error("New file name already exists!")

            else:
                st.error("File does not exist!")


    elif update_type == "Append Content":

        content = st.text_area("Enter content to append")

        if st.button("Append"):

            path = Path(filename)

            if path.exists():

                with open(path, "a") as file:
                    file.write("\n" + content)

                st.success("Content appended successfully!")

            else:
                st.error("File does not exist!")


    elif update_type == "Overwrite Content":

        content = st.text_area("Enter new content")

        if st.button("Overwrite"):

            path = Path(filename)

            if path.exists():

                with open(path, "w") as file:
                    file.write(content)

                st.success("File overwritten successfully!")

            else:
                st.error("File does not exist!")


# ---------------- DELETE FILE ----------------
elif operation == "Delete File":

    filename = st.text_input("Enter file name")

    if st.button("Delete File"):

        path = Path(filename)

        if path.exists():

            path.unlink()

            st.success("File deleted successfully!")

        else:
            st.error("File does not exist!")