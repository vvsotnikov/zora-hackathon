# Installation
First, install Git LFS: https://git-lfs.github.com/

Then check out the repository, create a conda environment, and 
install requirements:
```bash
conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
conda install -c conda-forge faiss-gpu
pip install ftfy regex tqdm streamlit
pip install git+https://github.com/openai/CLIP.git
```