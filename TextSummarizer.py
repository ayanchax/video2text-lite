from transformers import T5ForConditionalGeneration, T5Tokenizer

class TextSummarizer:
    def __init__(self, model_name="t5-small"):
        self.model = T5ForConditionalGeneration.from_pretrained(model_name)
        self.tokenizer = T5Tokenizer.from_pretrained(model_name)
    
    def summarize(self, prompt, transcription_text, max_length=150, min_length=40, length_penalty=2.0, num_beams=4):
        # Construct input with prompt and transcription text
        input_text = prompt + ": " + transcription_text
        
        # Tokenize the input text
        inputs = self.tokenizer.encode("summarize: " + input_text, return_tensors="pt", max_length=512, truncation=True)

        # Generate summary
        summary_ids = self.model.generate(inputs, max_length=max_length, min_length=min_length, length_penalty=length_penalty, num_beams=num_beams, early_stopping=True)

        # Decode and return the summary
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary



