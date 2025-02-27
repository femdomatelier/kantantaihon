import yaml


class Config:
    SE_SYMBOL = "○"
    CH_SYMBOL = "☆"
    POS_SYMBOL = "◆"
    AS_SYMBOL = "■"
    AE_SYMBOL = "■"
    AE_TEXT = "ここまで"

    @classmethod
    def load(cls, filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        cls.SE_SYMBOL = data.get('se_symbol', cls.SE_SYMBOL)
        cls.CH_SYMBOL = data.get('ch_symbol', cls.CH_SYMBOL)
        cls.AS_SYMBOL = data.get('as_symbol', cls.AS_SYMBOL)
        cls.AE_SYMBOL = data.get('ae_symbol', cls.AE_SYMBOL)
        cls.AE_TEXT = data.get('ae_text', cls.AE_TEXT)
