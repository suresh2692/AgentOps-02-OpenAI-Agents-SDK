import gradio as gr
from dotenv import load_dotenv

from sub_agents.supervisor import SupervisorAgent

load_dotenv(override=True)


async def run(query: str):
    # async for chunk in SupervisorAgent().run(query):
    #     yield chunk
    result = await SupervisorAgent().run(query)
    return result


with gr.Blocks(theme=gr.themes.Default(primary_hue="sky")) as ui:
    gr.Markdown("# Deep Research")
    query_textbox = gr.Textbox(label="What topic would you like to research?")
    run_button = gr.Button("Run", variant="primary")
    report = gr.Markdown(label="Report")

    run_button.click(fn=run, inputs=query_textbox, outputs=report)
    query_textbox.submit(fn=run, inputs=query_textbox, outputs=report)

ui.launch(inbrowser=True)
