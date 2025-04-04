# GPT-ImgEval: A Comprehensive Benchmark for Diagnosing GPT4o in Image Generation

![method](pipeline.jpg)

## 📰 News

* **[2025.4.3]**  🔥 We have released **GPT-ImgEval: A Comprehensive Benchmark forDiagnosing GPT4o in Image Generation**. Check out the [paper](https://arxiv.org/pdf/2504.02782). The code and dataset are coming soon

## 🏆 Contributions

**GPT-4o image generation evaluation：** The first benchmark to quantitatively and qualitatively evaluate GPT-4o’s image generation capabilities across three well-established benchmarks, including text-to-image generation（GenEval）, editing（Reason-Edit）, and world knowledge-informed semantic generation（WISE）. Our compre-hensive results highlight the superior image generation and comprehension capabilities of GPT4o over previous models.

**Generate Architecture Analysis：** Based on the benchmark results, we conducted an in-depth analysis of the potential underlying architecture of GPT-4o. Through classifier-based image analysis investigation, we confirmed that the decoder is most likely a Diffusion architecture and gave a potential Encoder paradigm speculation.

**More detailed analysis：** We present a detailed analysis of GPT-4o generation results and a systematic empirical study of its weaknesses, including common failure modes and generation artifacts.We further provide a comparative study of multi-round image editing capabilities between GPT-4o and Gemini 2.0 Flash. Additionally, we explore the AIGC safety issue by assessing the detectability of GPT-4o-generated images using existing SOTA image forensic models.

## 🤗 Dataset Download

We will upload our GPT-4o-based image synthesis results to Huggingface soon.
