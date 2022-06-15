# Text Generation Bot
how to install:
```bash
git clone
```
```python
pip install -r requirements.txt
```
```bash
echo TOKEN = 'Your token here' > config.py
```

Download weights [here](https://drive.google.com/drive/folders/1AlJiCt9beR42hOcZX9mdffxAoeAhkL1d?usp=sharing)
Add path to weights in lines 6 and 7 in models.py
```python
model_news = torch.load('YOUR PATH HERE')
model_congr = torch.load('YOUR PATH HERE')
```
run
```bash
python bot.py
```