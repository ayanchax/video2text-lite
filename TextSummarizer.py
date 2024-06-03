from transformers import T5ForConditionalGeneration, T5Tokenizer

class TextSummarizer:
    def __init__(self, model_name="t5-small"):
        self.model = T5ForConditionalGeneration.from_pretrained(model_name)
        self.tokenizer = T5Tokenizer.from_pretrained(model_name)
    
    def summarize(self, prompt, transcription_text, max_length=150, min_length=40, length_penalty=2.0, num_beams=4):
        """
    Generate a summary of the given transcription text using the T5 model.

    Parameters:
    prompt (str): The prompt to guide the summary generation.

    transcription_text (str): The text to summarize.

    max_length (int, optional): The maximum length of the summary. Defaults to 150.

    min_length (int, optional): The minimum length of the summary. Defaults to 40.

    length_penalty (float, optional): The penalty to apply to the length of the summary. Defaults to 2.0.
    
    num_beams (int, optional): The number of beams to use for beam search. Defaults to 4.

    Returns:
    str: The generated summary.
    """
        # Construct input with prompt and transcription text
        input_text = prompt + ": " + transcription_text
        
        # Tokenize the input text
        inputs = self.tokenizer.encode("summarize: " + input_text, return_tensors="pt", max_length=512, truncation=True)

        # Generate summary
        summary_ids = self.model.generate(inputs, max_length=max_length, min_length=min_length, length_penalty=length_penalty, num_beams=num_beams, early_stopping=True)

        # Decode and return the summary
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary



