import gradio as gr

# Data storage
books = []

# Add Book
def add_book(book_id, title, author):
    books.append({
        "id": book_id,
        "title": title,
        "author": author,
        "available": True
    })
    return "✅ Book Added Successfully"

# View Books
def view_books():
    if not books:
        return "No books available"
    
    result = ""
    for b in books:
        result += f"ID: {b['id']} | {b['title']} | {b['author']} | Available: {b['available']}\n"
    return result

# Issue Book
def issue_book(book_id):
    for b in books:
        if b["id"] == book_id:
            if b["available"]:
                b["available"] = False
                return "📕 Book Issued"
            else:
                return "⚠️ Already Issued"
    return "❌ Book Not Found"

# Return Book
def return_book(book_id):
    for b in books:
        if b["id"] == book_id:
            b["available"] = True
            return "📗 Book Returned"
    return "❌ Book Not Found"


# UI Layout
with gr.Blocks() as app:
    gr.Markdown("# 📚 Library Management System")

    with gr.Tab("Add Book"):
        book_id = gr.Textbox(label="Book ID")
        title = gr.Textbox(label="Title")
        author = gr.Textbox(label="Author")
        add_btn = gr.Button("Add Book")
        output1 = gr.Textbox()
        add_btn.click(add_book, [book_id, title, author], output1)

    with gr.Tab("View Books"):
        view_btn = gr.Button("Show Books")
        output2 = gr.Textbox(lines=10)
        view_btn.click(view_books, None, output2)

    with gr.Tab("Issue Book"):
        issue_id = gr.Textbox(label="Enter Book ID")
        issue_btn = gr.Button("Issue")
        output3 = gr.Textbox()
        issue_btn.click(issue_book, issue_id, output3)

    with gr.Tab("Return Book"):
        return_id = gr.Textbox(label="Enter Book ID")
        return_btn = gr.Button("Return")
        output4 = gr.Textbox()
        return_btn.click(return_book, return_id, output4)

app.launch()