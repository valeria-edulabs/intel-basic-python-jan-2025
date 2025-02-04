import gradio as gr

def calc_area(width, height):
    return f"The area is {width*height}"


demo = gr.Interface(
    fn=calc_area,
    inputs=["number", "number"],
    outputs=["textbox"]
)

demo.launch()