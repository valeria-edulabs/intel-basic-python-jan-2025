import gradio as gr

def calc_area(action, width, height):
    if action == 'Area':
        return f"The area is {width*height}", "HELLO"
    else:
        return f"The perimeter is {2*(width + height)}", "HELLO"


demo = gr.Interface(
    fn=calc_area,
    inputs=[
        gr.Dropdown(
            choices=['Area', 'Perimeter'],
            label='Select calculation:'
        ),
        gr.Number(
            label="Insert width:",
            minimum=1,
            maximum=1000
        ),
        "number"
    ],
    outputs=["textbox", "textbox"],
    title="My best App",
    description="My description",
    flagging_mode="never",
    theme='soft'
)

demo.launch(share=False)