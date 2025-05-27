## 💻 Automated GPT-4o Script (for Batch Data Processing)

The script supports **text-only** and **text+image** inputs, and it also supports automatically **saving the output images** and **response results**.

### Prerequisites

* macOS with M1/M2/M3/M4 chip
* [ChatGPT desktop app](https://chatgpt.com/download) installed

### Usage

* Since the window positions may vary for different users, it is recommended to first **obtain the approximate position** where the image appears, and then modify the obtained **x and y coordinates** in the *config.json* file to ensure proper functionality.

( Input an example in a window and use ***get_position.py*** to get the approximate position where the image appears. For more accurate positioning, we recommend scrolling the interface to the very bottom. The scroll parameters can also be set in the scroll_amount field of the *config.json* file. )

```bash
python get_position.py
```

* After modifying the *config.json*, you can run our sample code to try out the features of our script.

```bash
# text-only example
python chatgpt_script.py --config_path example/text-only

# text-image example 
# Please change the image_folder parameter in the config.json file under the example/text-image folder to the absolute path on your computer.
python chatgpt_script.py --config_path example/text-image
```

### Troubleshooting

If the tool isn't functioning correctly:

* Make sure ChatGPT app is installed and you're logged in.
* Verify that all required permissions have been granted.
* Make sure your current input method is set to English.
* Make sure the path of the image folder is an absolute path (using a relative path often leads to image input errors).

If you set a reasonable time interval based on the GPT-4o Pro account, you will rarely get synthesis failure results.


## ❤️ Acknowledgements

We would like to thank the following open-source projects and research works:

* [GenEval](https://github.com/djghosh13/geneval)
* [SmartEdit](https://github.com/TencentARC/SmartEdit)
* [WISE](https://github.com/PKU-YuanGroup/WISE)
* [claude-chatgpt-mcp](https://github.com/syedazharmbnr1/claude-chatgpt-mcp)
* [LLM-DepthEval](https://github.com/JiahaoZhang-Public/LLM-DepthEval)
* [awesome-framework-gallery](https://github.com/LongHZ140516/awesome-framework-gallery) 
* [GPT-ImgEval](https://github.com/PicoTrex/GPT-ImgEval) 
