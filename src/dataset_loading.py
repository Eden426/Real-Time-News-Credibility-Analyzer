import pandas as pd

def load_fake_news():
    fake_buzz = pd.read_csv('../data/raw_data/Fake_news/BuzzFeed_fake_news_content.csv')
    real_buzz = pd.read_csv('../data/raw_data/Fake_news/BuzzFeed_real_news_content.csv')
    fake_politifact = pd.read_csv('../data/raw_data/Fake_news/PolitiFact_fake_news_content.csv')
    real_politifact = pd.read_csv('../data/raw_data/Fake_news/PolitiFact_real_news_content.csv')
    return fake_buzz, real_buzz, fake_politifact, real_politifact

def load_isot():
    fake = pd.read_csv('../data/raw_data/isot/Fake.csv')
    real = pd.read_csv('../data/raw_data/isot/True.csv')
    return fake, real

def load_liar():
    liar_columns = [
        "id", "label", "statement", "subject", "speaker", "speaker_job_title",
        "state_info", "party_affiliation", "barely_true_counts", "false_counts",
        "half_true_counts", "mostly_true_counts", "pants_on_fire_counts", "context"
    ]
    train = pd.read_csv('../data/raw_data/liar/train.tsv', sep='\t', names=liar_columns, header=None)
    valid = pd.read_csv('../data/raw_data/liar/valid.tsv', sep='\t', names=liar_columns, header=None)
    test = pd.read_csv('../data/raw_data/liar/test.tsv', sep='\t', names=liar_columns, header=None)
    return train, valid, test