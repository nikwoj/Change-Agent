from setuptools import setup

setup(
    name='Multi_change',
    version='1.0',
    description='Vision Language Model forked from https://github.com/Chen-Yang-Liu/Change-Agent',
    url='https://github.com/nikwoj/Change-Agent.git',
    author='Nikolas Wojtalewicz',
    author_email='nikolas.wojtalewicz@visionsystemsinc.com',
    install_requires=[
        'mmcv==1.4.0',
        'ftfy',
        'timm',
        'mmengine==0.9.1',
        'mmsegmentation==0.13.0',
        # 'openai==1.3.4',
        # 'opencv-python==4.8.0.74',
        # 'opendatalab==0.0.10',
        # 'pandas==2.1.2',
        # 'pyarrow==14.0.0',
        # 'Pillow==10.0.1',
        'openai',
        'numpy',
        'opencv-python',
        'opendatalab',
        'Pillow',
        'pandas',
        'pyarrow',
        'torchaudio==2.0.2+cu118',
        'torch==2.0.1+cu118',
        'torchvision==0.15.2+cu118',
        'tqdm==4.66.4',
        'transformers==4.33.1',
        'scikit-image',
        'einops',
        'clip @ git+https://github.com/openai/CLIP.git@d50d76daa670286dd6cacf3bcd80b5e4823fc8e1',
        ], 
    packages=[
        'model','data','eval_func','utils_tool', 'multi_change_scripts',
        'models_CC','load_clsmodel',
        ],
)