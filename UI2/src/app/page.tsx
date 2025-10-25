"use client";

import Navigation from "@/components/Navigation";
import HeroSection from "@/components/HeroSection";
import AnalysisInterface from "@/components/AnalysisInterface";
import PhytochemicalBridge from "@/components/PhytochemicalBridge";
import SanskritTranslator from "@/components/SanskritTranslator";
import Timeline from "@/components/Timeline";
import Footer from "@/components/Footer";

export default function Home() {
  return (
    <main className="min-h-screen">
      <Navigation />
      <div id="home">
        <HeroSection />
      </div>
      <div id="analysis">
        <AnalysisInterface />
      </div>
      <div id="bridge">
        <PhytochemicalBridge />
      </div>
      <div id="translator">
        <SanskritTranslator />
      </div>
      <div id="timeline">
        <Timeline />
      </div>
      <Footer />
    </main>
  );
}
