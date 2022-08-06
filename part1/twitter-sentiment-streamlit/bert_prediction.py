from transformers import BertTokenizer
import torch.nn.utils.prune
from transformers import BertForSequenceClassification

label_dict = {1: 0, 2: 1}
bert_model = BertForSequenceClassification.from_pretrained(
     'bert-base-uncased',
     num_labels = len(label_dict),
     output_attentions=False,
     output_hidden_states=False
    )

def load_bert_model():
    print(' loading bert')
    model_dir = 'trained_models/'
    model_file = model_dir + 'BERT_ft_epoch7-aws.model'
    bert_model.load_state_dict(torch.load(model_file))
    bert_model.eval()


def encode_tweets(tweets):
    print(' In the encode tweets')
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    print('tokenizer')
    encoded_tweets = tokenizer.batch_encode_plus(
        tweets,
        add_special_tokens=True,
        return_attention_mask=True,
        padding=True,
        truncation=True,
        return_tensors='pt'
    )
    print('encoded_tweets', encoded_tweets)
    return encoded_tweets



def analyze_tweets_sentiment_with_bert(tweets):
    print(' In the analyze_tweets_sentiment_with_bert')
    sentiments = []
    encoded_tweets_data = encode_tweets(tweets)
    input_ids = encoded_tweets_data['input_ids']
    attention_masks = encoded_tweets_data['attention_mask']
    outputs = bert_model(input_ids, attention_masks)
    pred_logits = outputs.logits
    probs = pred_logits.softmax(dim=-1).detach().cpu().numpy().tolist()
    for prob in probs:
        if(prob[0] >= prob[1]):
            sentiments.append('Negative')
        else:
            sentiments.append('Positive')
    # print(len(sentiments))
    # for senti in sentiments:
    #     print(senti)
    # return sentiments

if __name__ =='__main__':
    load_bert_model()
