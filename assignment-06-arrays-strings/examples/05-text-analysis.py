"""
Assignment 6 - Example 5: Text Analysis
=======================================

This program demonstrates advanced text analysis techniques that are
essential for natural language processing, content analysis, and
information extraction. These skills are valuable for analyzing documents,
social media content, research data, and building intelligent applications.

Key Concepts Demonstrated:
- Text preprocessing and normalization
- Word frequency analysis and statistics
- Sentiment analysis and classification
- Text similarity and comparison
- Language pattern detection
- Document summarization techniques
- Content extraction and parsing
"""

import re
import string
from collections import Counter, defaultdict
import math

print("=== TEXT ANALYSIS TECHNIQUES ===")
print()

print("Text analysis enables extraction of meaningful insights from textual data:")
print("• Understand content patterns and themes")
print("• Analyze sentiment and emotional tone")
print("• Extract key information and summaries")
print("• Compare document similarity")
print("• Detect language patterns and anomalies")
print("• Support decision-making with text-based evidence")
print()

# TEXT PREPROCESSING AND NORMALIZATION
print("=== TEXT PREPROCESSING AND NORMALIZATION ===")
print()

def clean_text(text):
    """Comprehensive text cleaning for analysis."""
    # Convert to lowercase
    text = text.lower()
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Remove URLs
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
    
    # Remove email addresses
    text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '', text)
    
    # Remove numbers (optional)
    # text = re.sub(r'\d+', '', text)
    
    # Remove extra punctuation but keep sentence structure
    text = re.sub(r'[^\w\s.,!?;:-]', '', text)
    
    # Clean up spaces
    text = text.strip()
    
    return text

def tokenize_text(text, remove_stopwords=True, remove_punctuation=True):
    """Tokenize text into words with various options."""
    # Basic tokenization
    words = text.split()
    
    # Remove punctuation if requested
    if remove_punctuation:
        words = [word.strip(string.punctuation) for word in words]
        words = [word for word in words if word]  # Remove empty strings
    
    # Common English stopwords
    stopwords = {
        'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 
        'he', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'was', 
        'will', 'with', 'the', 'this', 'but', 'they', 'have', 'had', 'what', 
        'said', 'each', 'which', 'do', 'how', 'their', 'if', 'up', 'out', 'many',
        'then', 'them', 'these', 'so', 'some', 'her', 'would', 'make', 'like',
        'into', 'time', 'has', 'two', 'more', 'very', 'when', 'come', 'may',
        'its', 'over', 'think', 'also', 'your', 'work', 'life', 'only', 'can',
        'still', 'should', 'after', 'being', 'now', 'made', 'before', 'here',
        'through', 'when', 'where', 'much', 'go', 'me', 'back', 'with', 'well',
        'were', 'been', 'than'
    }
    
    # Remove stopwords if requested
    if remove_stopwords:
        words = [word for word in words if word.lower() not in stopwords]
    
    return words

def extract_sentences(text):
    """Extract sentences from text."""
    # Split on sentence endings
    sentences = re.split(r'[.!?]+', text)
    
    # Clean up sentences
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    
    return sentences

def normalize_text(text):
    """Normalize text for consistent analysis."""
    # Clean the text
    text = clean_text(text)
    
    # Handle common contractions
    contractions = {
        "won't": "will not",
        "can't": "cannot",
        "n't": " not",
        "'re": " are",
        "'ve": " have",
        "'ll": " will",
        "'d": " would",
        "'m": " am"
    }
    
    for contraction, expansion in contractions.items():
        text = text.replace(contraction, expansion)
    
    return text

# Demonstrate text preprocessing
print("Text Preprocessing Examples:")
sample_text = """
Hello World! This is a SAMPLE text for analysis. It contains URLs like 
https://example.com and email@domain.com. There are also numbers like 123 
and special characters @#$%. We'll test various preprocessing steps!
"""

print(f"Original text:")
print(f"  {repr(sample_text)}")
print()

cleaned = clean_text(sample_text)
print(f"Cleaned text:")
print(f"  {cleaned}")
print()

tokens = tokenize_text(cleaned)
print(f"Tokenized (no stopwords):")
print(f"  {tokens}")
print()

tokens_with_stopwords = tokenize_text(cleaned, remove_stopwords=False)
print(f"Tokenized (with stopwords):")
print(f"  {tokens_with_stopwords}")
print()

# WORD FREQUENCY ANALYSIS
print("=== WORD FREQUENCY ANALYSIS ===")
print()

def calculate_word_frequency(text, top_n=10):
    """Calculate word frequency statistics."""
    # Preprocess and tokenize
    normalized = normalize_text(text)
    words = tokenize_text(normalized)
    
    # Count frequencies
    word_counts = Counter(words)
    
    # Calculate statistics
    total_words = len(words)
    unique_words = len(word_counts)
    
    # Get most common words
    most_common = word_counts.most_common(top_n)
    
    # Calculate average word length
    avg_length = sum(len(word) for word in words) / len(words) if words else 0
    
    return {
        'total_words': total_words,
        'unique_words': unique_words,
        'vocabulary_richness': unique_words / total_words if total_words > 0 else 0,
        'average_word_length': round(avg_length, 2),
        'most_common': most_common,
        'word_counts': word_counts
    }

def analyze_word_patterns(text):
    """Analyze various word patterns in text."""
    words = tokenize_text(normalize_text(text), remove_stopwords=False)
    
    # Length distribution
    length_dist = Counter(len(word) for word in words)
    
    # Starting letters
    starting_letters = Counter(word[0].lower() for word in words if word)
    
    # Ending patterns
    endings = Counter(word[-2:].lower() for word in words if len(word) >= 2)
    
    # Find long words
    long_words = [word for word in words if len(word) > 7]
    
    return {
        'length_distribution': dict(length_dist.most_common()),
        'starting_letters': dict(starting_letters.most_common(10)),
        'common_endings': dict(endings.most_common(10)),
        'long_words': long_words[:20],  # Top 20 longest
    }

# Demonstrate word frequency analysis
print("Word Frequency Analysis Examples:")

article_text = """
Artificial intelligence and machine learning are transforming the technology industry. 
These technologies enable computers to learn from data and make intelligent decisions. 
Machine learning algorithms can process vast amounts of information and identify patterns 
that humans might miss. Deep learning, a subset of machine learning, uses neural networks 
to simulate human brain processing. Companies are investing heavily in AI research and 
development. The applications of artificial intelligence span across healthcare, finance, 
transportation, and entertainment. As these technologies continue to evolve, they promise 
to revolutionize how we work, live, and interact with the digital world.
"""

print("Analyzing article about AI and machine learning:")
freq_analysis = calculate_word_frequency(article_text, top_n=15)

print(f"Text Statistics:")
print(f"  Total words: {freq_analysis['total_words']}")
print(f"  Unique words: {freq_analysis['unique_words']}")
print(f"  Vocabulary richness: {freq_analysis['vocabulary_richness']:.3f}")
print(f"  Average word length: {freq_analysis['average_word_length']}")
print()

print(f"Most common words:")
for word, count in freq_analysis['most_common']:
    percentage = (count / freq_analysis['total_words']) * 100
    print(f"  {word}: {count} ({percentage:.1f}%)")
print()

# Analyze word patterns
patterns = analyze_word_patterns(article_text)
print("Word Pattern Analysis:")
print(f"  Length distribution: {patterns['length_distribution']}")
print(f"  Common starting letters: {dict(list(patterns['starting_letters'].items())[:5])}")
print(f"  Long words: {patterns['long_words'][:10]}")
print()

# SENTIMENT ANALYSIS
print("=== SENTIMENT ANALYSIS ===")
print()

def simple_sentiment_analysis(text):
    """Perform basic sentiment analysis using word lists."""
    # Simple positive and negative word lists
    positive_words = {
        'good', 'great', 'excellent', 'amazing', 'wonderful', 'fantastic', 
        'awesome', 'brilliant', 'outstanding', 'superb', 'magnificent',
        'perfect', 'beautiful', 'love', 'enjoy', 'happy', 'pleased',
        'satisfied', 'delighted', 'thrilled', 'excited', 'optimistic',
        'positive', 'impressive', 'remarkable', 'extraordinary', 'success',
        'win', 'victory', 'triumph', 'achieve', 'accomplish', 'improve',
        'benefit', 'advantage', 'profit', 'gain', 'valuable', 'useful'
    }
    
    negative_words = {
        'bad', 'terrible', 'awful', 'horrible', 'disgusting', 'hate',
        'dislike', 'angry', 'sad', 'unhappy', 'disappointed', 'frustrated',
        'annoyed', 'irritated', 'upset', 'worried', 'concerned', 'problem',
        'issue', 'difficulty', 'trouble', 'fail', 'failure', 'lose',
        'loss', 'defeat', 'disaster', 'crisis', 'damage', 'harm',
        'hurt', 'pain', 'suffer', 'struggle', 'challenge', 'obstacle',
        'negative', 'poor', 'worse', 'worst', 'decline', 'decrease'
    }
    
    # Tokenize and count sentiment words
    words = tokenize_text(normalize_text(text))
    
    positive_count = sum(1 for word in words if word in positive_words)
    negative_count = sum(1 for word in words if word in negative_words)
    total_sentiment_words = positive_count + negative_count
    
    # Calculate sentiment score
    if total_sentiment_words == 0:
        sentiment_score = 0
        sentiment_label = "Neutral"
    else:
        sentiment_score = (positive_count - negative_count) / total_sentiment_words
        if sentiment_score > 0.2:
            sentiment_label = "Positive"
        elif sentiment_score < -0.2:
            sentiment_label = "Negative"
        else:
            sentiment_label = "Neutral"
    
    return {
        'sentiment_score': round(sentiment_score, 3),
        'sentiment_label': sentiment_label,
        'positive_words_found': positive_count,
        'negative_words_found': negative_count,
        'confidence': abs(sentiment_score)
    }

def analyze_sentiment_by_sentence(text):
    """Analyze sentiment of each sentence in the text."""
    sentences = extract_sentences(text)
    sentence_sentiments = []
    
    for i, sentence in enumerate(sentences):
        sentiment = simple_sentiment_analysis(sentence)
        sentence_sentiments.append({
            'sentence_number': i + 1,
            'sentence': sentence[:100] + "..." if len(sentence) > 100 else sentence,
            'sentiment': sentiment['sentiment_label'],
            'score': sentiment['sentiment_score']
        })
    
    return sentence_sentiments

# Demonstrate sentiment analysis
print("Sentiment Analysis Examples:")

# Positive review
positive_review = """
This product is absolutely amazing! I love how easy it is to use and the quality 
is outstanding. The customer service was excellent and very helpful. I'm extremely 
satisfied with my purchase and would definitely recommend it to others. Great value 
for money and fast shipping. This company really knows how to make customers happy!
"""

# Negative review
negative_review = """
I'm very disappointed with this purchase. The product arrived damaged and doesn't 
work as advertised. The quality is terrible and feels cheap. Customer service was 
unhelpful and rude when I tried to get a refund. This was a complete waste of money 
and I regret buying it. I would not recommend this to anyone. Awful experience!
"""

# Mixed review
mixed_review = """
The product has some good features and works well for basic tasks. However, there 
are several issues that are concerning. The build quality could be better and the 
price seems a bit high for what you get. Customer service was okay but not great. 
It's an average product that might work for some people but not for others.
"""

reviews = [
    ("Positive Review", positive_review),
    ("Negative Review", negative_review),
    ("Mixed Review", mixed_review)
]

for review_type, review_text in reviews:
    sentiment = simple_sentiment_analysis(review_text)
    print(f"{review_type}:")
    print(f"  Sentiment: {sentiment['sentiment_label']}")
    print(f"  Score: {sentiment['sentiment_score']}")
    print(f"  Positive words: {sentiment['positive_words_found']}")
    print(f"  Negative words: {sentiment['negative_words_found']}")
    print(f"  Confidence: {sentiment['confidence']:.3f}")
    print()

# TEXT SIMILARITY AND COMPARISON
print("=== TEXT SIMILARITY AND COMPARISON ===")
print()

def calculate_jaccard_similarity(text1, text2):
    """Calculate Jaccard similarity between two texts."""
    words1 = set(tokenize_text(normalize_text(text1)))
    words2 = set(tokenize_text(normalize_text(text2)))
    
    intersection = len(words1 & words2)
    union = len(words1 | words2)
    
    return intersection / union if union > 0 else 0

def calculate_cosine_similarity(text1, text2):
    """Calculate cosine similarity between two texts."""
    words1 = tokenize_text(normalize_text(text1))
    words2 = tokenize_text(normalize_text(text2))
    
    # Create word frequency vectors
    all_words = set(words1 + words2)
    vector1 = [words1.count(word) for word in all_words]
    vector2 = [words2.count(word) for word in all_words]
    
    # Calculate cosine similarity
    dot_product = sum(a * b for a, b in zip(vector1, vector2))
    magnitude1 = math.sqrt(sum(a * a for a in vector1))
    magnitude2 = math.sqrt(sum(a * a for a in vector2))
    
    if magnitude1 == 0 or magnitude2 == 0:
        return 0
    
    return dot_product / (magnitude1 * magnitude2)

def find_common_themes(texts):
    """Find common themes across multiple texts."""
    all_words = []
    for text in texts:
        words = tokenize_text(normalize_text(text))
        all_words.extend(words)
    
    # Find words that appear in multiple texts
    word_counts = Counter(all_words)
    text_appearances = defaultdict(int)
    
    for text in texts:
        words_in_text = set(tokenize_text(normalize_text(text)))
        for word in words_in_text:
            text_appearances[word] += 1
    
    # Find words that appear in at least half the texts
    min_appearances = len(texts) // 2 + 1
    common_themes = {word: count for word, count in text_appearances.items() 
                    if count >= min_appearances and word_counts[word] >= 2}
    
    return sorted(common_themes.items(), key=lambda x: x[1], reverse=True)

# Demonstrate text similarity
print("Text Similarity Examples:")

tech_article1 = """
Machine learning is revolutionizing the technology industry. Companies are using 
artificial intelligence to improve their products and services. Deep learning 
algorithms can process large datasets and identify complex patterns.
"""

tech_article2 = """
Artificial intelligence and machine learning are transforming how businesses operate. 
These technologies enable automation and intelligent decision-making. Neural networks 
and deep learning are particularly powerful for pattern recognition tasks.
"""

different_topic = """
Climate change is one of the most pressing issues of our time. Global warming is 
causing extreme weather patterns and rising sea levels. We need immediate action 
to reduce carbon emissions and protect our environment.
"""

# Calculate similarities
jaccard_sim_tech = calculate_jaccard_similarity(tech_article1, tech_article2)
cosine_sim_tech = calculate_cosine_similarity(tech_article1, tech_article2)

jaccard_sim_diff = calculate_jaccard_similarity(tech_article1, different_topic)
cosine_sim_diff = calculate_cosine_similarity(tech_article1, different_topic)

print("Similarity between tech articles:")
print(f"  Jaccard similarity: {jaccard_sim_tech:.3f}")
print(f"  Cosine similarity: {cosine_sim_tech:.3f}")
print()

print("Similarity between tech article and climate article:")
print(f"  Jaccard similarity: {jaccard_sim_diff:.3f}")
print(f"  Cosine similarity: {cosine_sim_diff:.3f}")
print()

# Find common themes
texts_for_themes = [tech_article1, tech_article2]
common_themes = find_common_themes(texts_for_themes)
print("Common themes in tech articles:")
for theme, appearances in common_themes[:10]:
    print(f"  {theme}: appears in {appearances} texts")
print()

# DOCUMENT SUMMARIZATION
print("=== DOCUMENT SUMMARIZATION ===")
print()

def extract_key_sentences(text, num_sentences=3):
    """Extract key sentences for summarization based on word frequency."""
    sentences = extract_sentences(text)
    if len(sentences) <= num_sentences:
        return sentences
    
    # Calculate word frequencies
    words = tokenize_text(normalize_text(text))
    word_freq = Counter(words)
    
    # Score sentences based on word frequencies
    sentence_scores = []
    for i, sentence in enumerate(sentences):
        sentence_words = tokenize_text(normalize_text(sentence))
        score = sum(word_freq[word] for word in sentence_words)
        # Normalize by sentence length
        score = score / len(sentence_words) if sentence_words else 0
        sentence_scores.append((score, i, sentence))
    
    # Sort by score and return top sentences
    sentence_scores.sort(reverse=True)
    selected_sentences = sorted(sentence_scores[:num_sentences], key=lambda x: x[1])
    
    return [sentence for _, _, sentence in selected_sentences]

def generate_word_cloud_data(text, top_n=20):
    """Generate data for word cloud visualization."""
    freq_analysis = calculate_word_frequency(text, top_n=top_n)
    word_counts = freq_analysis['word_counts']
    
    # Scale frequencies for visualization
    max_freq = max(word_counts.values()) if word_counts else 1
    scaled_words = {word: (count / max_freq) * 100 
                   for word, count in word_counts.most_common(top_n)}
    
    return scaled_words

def extract_entities(text):
    """Extract potential entities (names, places, organizations) using simple patterns."""
    # Capitalized words (potential proper nouns)
    capitalized_pattern = r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b'
    potential_entities = re.findall(capitalized_pattern, text)
    
    # Filter out common words that might be capitalized
    common_capitalized = {'The', 'This', 'That', 'These', 'Those', 'A', 'An'}
    entities = [entity for entity in potential_entities 
               if entity not in common_capitalized]
    
    # Count frequencies
    entity_counts = Counter(entities)
    
    return dict(entity_counts.most_common())

# Demonstrate document summarization
print("Document Summarization Examples:")

long_article = """
Artificial intelligence has become one of the most transformative technologies of the 21st century. 
The field encompasses machine learning, deep learning, natural language processing, and computer vision. 
Companies across industries are investing billions of dollars in AI research and development. 
Machine learning algorithms can analyze vast amounts of data to identify patterns and make predictions. 
Deep learning uses neural networks with multiple layers to simulate human brain processing. 
Natural language processing enables computers to understand and generate human language. 
Computer vision allows machines to interpret and analyze visual information from images and videos. 
The applications of AI span healthcare, finance, transportation, entertainment, and manufacturing. 
In healthcare, AI assists in medical diagnosis, drug discovery, and personalized treatment plans. 
Financial institutions use AI for fraud detection, algorithmic trading, and risk assessment. 
Autonomous vehicles rely on AI for navigation, object detection, and decision-making. 
Entertainment platforms use recommendation systems to personalize content for users. 
Manufacturing companies implement AI for quality control, predictive maintenance, and supply chain optimization. 
However, the rapid advancement of AI also raises important ethical and social concerns. 
Issues include job displacement, privacy concerns, algorithmic bias, and the need for transparency. 
Researchers and policymakers are working to address these challenges through responsible AI development. 
The future of artificial intelligence promises even more sophisticated capabilities and applications. 
As AI continues to evolve, it will likely reshape how we work, live, and interact with technology.
"""

print("Original article length:", len(extract_sentences(long_article)), "sentences")
print()

# Extract key sentences
key_sentences = extract_key_sentences(long_article, num_sentences=4)
print("Key sentences summary:")
for i, sentence in enumerate(key_sentences, 1):
    print(f"  {i}. {sentence}")
print()

# Generate word cloud data
word_cloud_data = generate_word_cloud_data(long_article, top_n=15)
print("Word cloud data (scaled frequencies):")
for word, frequency in sorted(word_cloud_data.items(), key=lambda x: x[1], reverse=True):
    print(f"  {word}: {frequency:.1f}")
print()

# Extract entities
entities = extract_entities(long_article)
print("Potential entities found:")
for entity, count in list(entities.items())[:10]:
    print(f"  {entity}: {count}")
print()

# LANGUAGE PATTERN DETECTION
print("=== LANGUAGE PATTERN DETECTION ===")
print()

def detect_writing_style(text):
    """Analyze writing style characteristics."""
    sentences = extract_sentences(text)
    words = tokenize_text(normalize_text(text), remove_stopwords=False)
    
    # Sentence statistics
    sentence_lengths = [len(tokenize_text(sentence, remove_stopwords=False)) 
                       for sentence in sentences]
    avg_sentence_length = sum(sentence_lengths) / len(sentence_lengths) if sentence_lengths else 0
    
    # Word statistics
    word_lengths = [len(word) for word in words]
    avg_word_length = sum(word_lengths) / len(word_lengths) if word_lengths else 0
    
    # Complexity indicators
    long_sentences = sum(1 for length in sentence_lengths if length > 20)
    long_words = sum(1 for length in word_lengths if length > 6)
    
    # Punctuation usage
    punctuation_count = sum(1 for char in text if char in '.,!?;:')
    exclamation_count = text.count('!')
    question_count = text.count('?')
    
    return {
        'avg_sentence_length': round(avg_sentence_length, 1),
        'avg_word_length': round(avg_word_length, 1),
        'total_sentences': len(sentences),
        'total_words': len(words),
        'long_sentences_ratio': round(long_sentences / len(sentences), 3) if sentences else 0,
        'long_words_ratio': round(long_words / len(words), 3) if words else 0,
        'punctuation_density': round(punctuation_count / len(text), 3),
        'exclamation_ratio': round(exclamation_count / len(sentences), 3) if sentences else 0,
        'question_ratio': round(question_count / len(sentences), 3) if sentences else 0,
    }

def detect_readability_level(text):
    """Estimate readability level using simple metrics."""
    style = detect_writing_style(text)
    
    # Simple readability score (0-10 scale)
    complexity_score = 0
    
    # Sentence length factor
    if style['avg_sentence_length'] > 25:
        complexity_score += 3
    elif style['avg_sentence_length'] > 15:
        complexity_score += 2
    elif style['avg_sentence_length'] > 10:
        complexity_score += 1
    
    # Word length factor
    if style['avg_word_length'] > 6:
        complexity_score += 3
    elif style['avg_word_length'] > 5:
        complexity_score += 2
    elif style['avg_word_length'] > 4:
        complexity_score += 1
    
    # Long words factor
    if style['long_words_ratio'] > 0.3:
        complexity_score += 2
    elif style['long_words_ratio'] > 0.2:
        complexity_score += 1
    
    # Determine readability level
    if complexity_score <= 2:
        level = "Elementary"
    elif complexity_score <= 4:
        level = "Middle School"
    elif complexity_score <= 6:
        level = "High School"
    elif complexity_score <= 8:
        level = "College"
    else:
        level = "Graduate"
    
    return {
        'complexity_score': complexity_score,
        'readability_level': level,
        'style_metrics': style
    }

# Demonstrate language pattern detection
print("Language Pattern Detection Examples:")

# Simple text (elementary level)
simple_text = """
I like dogs. Dogs are fun pets. They play and run. They are good friends. 
My dog is brown. He likes to play fetch. We go to the park every day. 
The park is big. Other dogs play there too. It is a happy place.
"""

# Complex text (college level)
complex_text = """
The interdisciplinary nature of contemporary research necessitates a comprehensive 
understanding of methodological approaches that transcend traditional academic boundaries. 
Researchers must navigate increasingly sophisticated theoretical frameworks while 
maintaining methodological rigor throughout their investigative processes. 
The integration of quantitative and qualitative paradigms presents both opportunities 
and challenges for scholars seeking to address multifaceted research questions.
"""

texts_to_analyze = [
    ("Simple Text", simple_text),
    ("Complex Text", complex_text),
    ("Previous AI Article", long_article[:500])  # First 500 chars
]

for text_name, text_sample in texts_to_analyze:
    readability = detect_readability_level(text_sample)
    style = readability['style_metrics']
    
    print(f"{text_name}:")
    print(f"  Readability Level: {readability['readability_level']}")
    print(f"  Complexity Score: {readability['complexity_score']}/10")
    print(f"  Average Sentence Length: {style['avg_sentence_length']} words")
    print(f"  Average Word Length: {style['avg_word_length']} characters")
    print(f"  Long Words Ratio: {style['long_words_ratio']}")
    print()

print("=== SUMMARY ===")
print()
print("Text Analysis Summary:")
print("1. Text preprocessing is essential for accurate analysis")
print("2. Word frequency analysis reveals content themes and patterns")
print("3. Sentiment analysis helps understand emotional tone")
print("4. Text similarity enables document comparison and clustering")
print("5. Summarization extracts key information from long texts")
print("6. Style analysis provides insights into writing characteristics")
print("7. Pattern detection helps classify and categorize content")
print("8. These techniques form the foundation of natural language processing")

"""
KEY TAKEAWAYS:
==============
1. Text preprocessing significantly impacts analysis quality
2. Multiple similarity metrics provide different perspectives
3. Simple sentiment analysis can be surprisingly effective
4. Word frequency reveals important content patterns
5. Summarization helps extract key information quickly
6. Writing style analysis enables content classification
7. Regular expressions are powerful for pattern extraction
8. Consider context and domain when interpreting results

TEXT PREPROCESSING STEPS:
=========================
1. Convert to lowercase for consistency
2. Remove or handle special characters
3. Tokenize into words or sentences
4. Remove stopwords (optional)
5. Handle contractions and abbreviations
6. Normalize whitespace and punctuation

ANALYSIS TECHNIQUES:
====================
• Frequency Analysis: Word counts and distributions
• Sentiment Analysis: Emotional tone detection
• Similarity Measures: Jaccard, cosine, edit distance
• Topic Modeling: Theme identification
• Entity Extraction: Named entity recognition
• Style Analysis: Writing characteristic measurement

APPLICATIONS:
=============
• Social media monitoring and analysis
• Customer feedback analysis
• Document classification and search
• Content recommendation systems
• Automated summarization
• Language learning and assessment
• Market research and competitor analysis
• Academic research and literature review

PERFORMANCE CONSIDERATIONS:
===========================
• Preprocessing can be computationally expensive
• Consider memory usage with large text collections
• Cache results of expensive operations
• Use appropriate data structures (sets, counters)
• Consider parallel processing for large datasets

LIMITATIONS AND CHALLENGES:
===========================
• Context and sarcasm are difficult to detect
• Domain-specific language requires specialized handling
• Multilingual text needs different approaches
• Bias in training data affects results
• Cultural and regional language variations

NEXT STEP:
Go to 06-complete-program.py to see a comprehensive application combining all concepts!
"""