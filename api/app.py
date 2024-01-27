# app.py

import asyncio
from flask import Flask, jsonify, request
from flask_cors import CORS
from obsei.source.youtube_scrapper import YoutubeScrapperSource, YoutubeScrapperConfig
from obsei.analyzer.classification_analyzer import (
    ClassificationAnalyzerConfig,
    ZeroShotClassificationAnalyzer,
)
from obsei.sink.pandas_sink import PandasSink, PandasSinkConfig
import pandas as pd

app = Flask(__name__)
CORS(app)

async def analyze_youtube_async(video_url):
    source_config = YoutubeScrapperConfig(
        video_url=video_url,
        fetch_replies=False,
        max_comments=20,
        lookup_period="1Y",
    )
    source = YoutubeScrapperSource()
    source_response_list = source.lookup(source_config)

    text_analyzer = ZeroShotClassificationAnalyzer(
        model_name_or_path="typeform/mobilebert-uncased-mnli", device="auto"
    )
    analyzer_response_list = text_analyzer.analyze_input(
        source_response_list=source_response_list,
        analyzer_config=ClassificationAnalyzerConfig(labels=["positive", "negative"]),
    )

    sink_config = PandasSinkConfig(dataframe=pd.DataFrame())
    sink = PandasSink()
    dataframe = sink.send_data(analyzer_response_list, sink_config)

    # Calculate positive and negative counts
    positive_count = dataframe['segmented_data_classifier_data_positive'].astype('float').sum()
    negative_count = dataframe['segmented_data_classifier_data_negative'].astype('float').sum()

    # Calculate percentages
    total_count = positive_count + negative_count
    positive_percentage = (positive_count / total_count) * 100
    negative_percentage = (negative_count / total_count) * 100

    result = {
        'positive_percentage': positive_percentage,
        'negative_percentage': negative_percentage,
    }

    return result

@app.route('/analyze_youtube', methods=['POST'])
def analyze_youtube():
    data = request.get_json()
    video_url = data.get('video_url')

    # Run the asynchronous analysis within the Flask event loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(analyze_youtube_async(video_url))
    loop.close()

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
