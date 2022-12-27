import sys
from pathlib import Path

file = Path(sys.argv[1])
file.write_text(
  file.read_text()\
  .replace('    return demo', """
    with demo:
        gr.Markdown(
          'Created by [AUTOMATIC1111 / stable-diffusion-webui-docker](https://github.com/skrashevich/stable-diffusion-webui)'
        )
    return demo
""", 1)
)
