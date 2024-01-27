# **Youtube Comment Analyzer**

## Overview

YouTube Comment Sentiment Analyzer is a Flask-based web application that leverages [Obsei](https://github.com/obsei/obsei), an open-source low-code AI-powered automation tool, to perform sentiment analysis on comments from a given YouTube video. The application exposes an API endpoint that receives a YouTube video URL, analyzes the sentiments of comments related to the video, and returns the positive and negative sentiment percentages.

## Features

- **Sentiment Analysis:** Analyze sentiments of comments for a given YouTube video.
- **Flask Backend:** Provides an API endpoint for receiving video URLs and returning sentiment percentages.
- **Obsei:** An open-source low-code AI-powered automation tool utilized for sentiment analysis.
- **Pandas Sink:** Stores the analyzed data in a Pandas DataFrame.

## How It Works

1. The user sends a POST request to the `/analyze_youtube` endpoint with a JSON payload containing the YouTube video URL.
2. The Flask server extracts the video URL from the payload.
3. An asynchronous analysis is performed using Obsei to analyze sentiments of comments related to the provided video URL.
4. The positive and negative sentiment percentages are calculated based on the analysis.
5. The result, including positive and negative percentages, is returned as a JSON response.

## Tech Stack

- **Flask:** Python web framework for building the backend server.
- **Obsei:** An open-source low-code AI-powered automation tool for sentiment analysis.
- **Pandas:** Data manipulation library for Python.
- **Next.js:** Frontend framework for building user interfaces.

## UI
#### Before Submission
![image](https://github.com/kajalchoudhary1003/Youtube_Comment_Analyzer/assets/108188712/52a4bf91-2b36-4e2e-8d56-f4f251cb257b)

#### After Submission
![image](https://github.com/kajalchoudhary1003/Youtube_Comment_Analyzer/assets/108188712/079ecee6-2674-497b-9230-b8dd2aeeed00)



