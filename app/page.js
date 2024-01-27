'use client'
import Image from "next/image";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import "./globals.css";
import { useState } from "react";


export default function Home() {
  const [videoUrl, setVideoUrl] = useState('');
  const [result, setResult] = useState(null);

  const handleAnalyze = async () => {
    try {
      const response = await fetch('http://localhost:5000/analyze_youtube', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ video_url: videoUrl }),
      });

      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error('Error analyzing YouTube video:', error);
    }
  };
  return (
    <>
      <main className="flex pt-20 flex-col items-center bg-back h-screen w-screen">
        <h1 className="animate-character font-bold tracking-normal lg:text-7xl md:text-5xl sm:text-5xl min-[320px]:text-3xl">
          Enter Youtube URL Link
        </h1>

        <Input
          type="url"
          placeholder="URL"
          value={videoUrl}
          onChange={(e) => setVideoUrl(e.target.value)}
          className="lg:w-6/12 md:w-6/12 sm:w-6/12 min-[320px]:w-3/4 mt-5 text-lg ring-2 ring-slate-500 focus-visible:ring-orange-600 focus-visible:ring-2 rounded-md"
        />

        <Button
        onClick ={handleAnalyze}
          variant="outline"
          className="mt-5 border-0 border-none border-transparent  rounded-full bg-violet-900 hover:bg-violet-700 text-white hover:text-white"
        >
          Submit
        </Button>
        {result && (
        <div className="mt-5 text-lg">
          
          <p className="text-green-600 font-semibold">Positive Percentage: {result.positive_percentage.toFixed(2)}%</p>
          <p className="text-red-500 font-semibold">Negative Percentage: {result.negative_percentage.toFixed(2)}%</p>
        </div>
      )}
      </main>
      
    </>
  );
}
