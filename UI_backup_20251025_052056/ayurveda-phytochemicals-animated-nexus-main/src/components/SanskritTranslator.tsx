"use client";

import { motion } from "framer-motion";
import { useState } from "react";
import { Card } from "@/components/ui/card";
import { Textarea } from "@/components/ui/textarea";
import { Button } from "@/components/ui/button";
import { Languages, Sparkles, Copy, Check } from "lucide-react";
import { apiService, AnalysisResponse } from "@/lib/api";

export default function SanskritTranslator() {
  const [sanskritText, setSanskritText] = useState("");
  const [translation, setTranslation] = useState("");
  const [isTranslating, setIsTranslating] = useState(false);
  const [copied, setCopied] = useState(false);
  const [analysisResults, setAnalysisResults] = useState<AnalysisResponse | null>(null);

  const handleTranslate = async () => {
    if (!sanskritText.trim()) return;
    
    setIsTranslating(true);
    try {
      const response = await apiService.analyzeText(sanskritText);
      setAnalysisResults(response);
      
      // Format the analysis results for display
      const formattedResults = response.results.map(result => {
        const herb = result.herb;
        const compounds = result.compounds;
        const hypotheses = result.hypotheses;
        
        return `
Herb: ${herb.name}
Properties: ${herb.rasa?.join(', ') || 'N/A'}
Compounds: ${compounds.map(c => c.name || c.cid).join(', ')}
Hypotheses: ${hypotheses.map(h => h.title || h.summary).join('; ')}
        `.trim();
      }).join('\n\n');
      
      setTranslation(`Analysis Results:\n\n${formattedResults}`);
    } catch (error) {
      console.error('Translation error:', error);
      setTranslation("Error: Unable to analyze the text. Please check your connection and try again.");
    } finally {
      setIsTranslating(false);
    }
  };

  const handleCopy = () => {
    navigator.clipboard.writeText(translation);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <section className="py-24 px-6 bg-gradient-to-br from-amber-50 via-orange-50 to-yellow-50 dark:from-amber-950 dark:via-orange-950 dark:to-yellow-950">
      <div className="max-w-6xl mx-auto">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8 }}
          className="text-center mb-16"
        >
          <motion.div
            animate={{ rotate: [0, 10, -10, 0] }}
            transition={{ duration: 3, repeat: Infinity }}
            className="inline-block mb-6"
          >
            <Languages size={60} className="text-primary" />
          </motion.div>
          <h2 className="font-cinzel text-4xl md:text-5xl font-bold mb-6 text-foreground">
            Sanskrit Translator
          </h2>
          <p className="text-xl text-muted-foreground max-w-3xl mx-auto">
            Decode ancient Ayurvedic texts and unlock the wisdom of centuries
          </p>
          <p className="font-devanagari text-2xl mt-4 text-primary">
            संस्कृत अनुवादक
          </p>
        </motion.div>

        <div className="grid md:grid-cols-2 gap-8">
          {/* Sanskrit Input */}
          <motion.div
            initial={{ opacity: 0, x: -50 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.8, delay: 0.2 }}
          >
            <Card className="p-6 h-full backdrop-blur-sm bg-card/80 border-2 border-primary/20 shadow-xl hover:shadow-2xl transition-shadow">
              <div className="flex items-center gap-3 mb-4">
                <motion.div
                  animate={{ scale: [1, 1.2, 1] }}
                  transition={{ duration: 2, repeat: Infinity }}
                >
                  <Sparkles className="text-primary" size={24} />
                </motion.div>
                <h3 className="font-cinzel text-2xl font-semibold">Sanskrit Text</h3>
              </div>
              <Textarea
                placeholder="Paste your Sanskrit script here... (e.g., आयुर्वेदः अमृतानां शास्त्रम्)"
                className="min-h-[300px] font-devanagari text-lg resize-none border-2 border-primary/30 focus:border-primary transition-colors"
                value={sanskritText}
                onChange={(e) => setSanskritText(e.target.value)}
              />
              <motion.div whileHover={{ scale: 1.02 }} whileTap={{ scale: 0.98 }} className="mt-4">
                <Button
                  onClick={handleTranslate}
                  disabled={!sanskritText || isTranslating}
                  className="w-full bg-primary text-primary-foreground hover:bg-primary/90 py-6 text-lg font-semibold shadow-lg"
                >
                  {isTranslating ? (
                    <motion.div
                      animate={{ rotate: 360 }}
                      transition={{ duration: 1, repeat: Infinity, ease: "linear" }}
                      className="mr-2"
                    >
                      <Sparkles size={20} />
                    </motion.div>
                  ) : (
                    <Languages size={20} className="mr-2" />
                  )}
                  {isTranslating ? "Translating..." : "Translate"}
                </Button>
              </motion.div>
            </Card>
          </motion.div>

          {/* Translation Output */}
          <motion.div
            initial={{ opacity: 0, x: 50 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.8, delay: 0.4 }}
          >
            <Card className="p-6 h-full backdrop-blur-sm bg-card/80 border-2 border-accent/20 shadow-xl hover:shadow-2xl transition-shadow">
              <div className="flex items-center justify-between mb-4">
                <div className="flex items-center gap-3">
                  <motion.div
                    animate={{ scale: [1, 1.2, 1] }}
                    transition={{ duration: 2, repeat: Infinity, delay: 0.5 }}
                  >
                    <Sparkles className="text-accent" size={24} />
                  </motion.div>
                  <h3 className="font-cinzel text-2xl font-semibold">Translation</h3>
                </div>
                {translation && (
                  <motion.div whileHover={{ scale: 1.1 }} whileTap={{ scale: 0.9 }}>
                    <Button
                      onClick={handleCopy}
                      variant="ghost"
                      size="icon"
                      className="text-accent hover:text-accent/80"
                    >
                      {copied ? <Check size={20} /> : <Copy size={20} />}
                    </Button>
                  </motion.div>
                )}
              </div>
              <div className="min-h-[300px] p-4 bg-muted/50 rounded-lg border-2 border-accent/30">
                {translation ? (
                  <motion.p
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    transition={{ duration: 0.5 }}
                    className="text-lg leading-relaxed"
                  >
                    {translation}
                  </motion.p>
                ) : (
                  <motion.div
                    animate={{ opacity: [0.3, 0.6, 0.3] }}
                    transition={{ duration: 2, repeat: Infinity }}
                    className="h-full flex items-center justify-center text-muted-foreground text-center"
                  >
                    <p>Your translation will appear here...</p>
                  </motion.div>
                )}
              </div>
            </Card>
          </motion.div>
        </div>

        {/* Example Texts */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8, delay: 0.6 }}
          className="mt-12"
        >
          <h4 className="font-cinzel text-xl font-semibold mb-4 text-center">Example Sanskrit Texts</h4>
          <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-4">
            {[
              { sanskrit: "आयुर्वेदः अमृतानां शास्त्रम्", translation: "Ayurveda is the science of life" },
              { sanskrit: "यथा पिण्डे तथा ब्रह्माण्डे", translation: "As is the microcosm, so is the macrocosm" },
              { sanskrit: "सर्वे भवन्तु सुखिनः", translation: "May all beings be happy" },
            ].map((example, index) => (
              <motion.div
                key={index}
                whileHover={{ scale: 1.05, y: -5 }}
                className="cursor-pointer"
                onClick={() => setSanskritText(example.sanskrit)}
              >
                <Card className="p-4 bg-card/60 backdrop-blur-sm border border-primary/20 hover:border-primary/50 transition-colors">
                  <p className="font-devanagari text-lg mb-2 text-primary">{example.sanskrit}</p>
                  <p className="text-sm text-muted-foreground italic">{example.translation}</p>
                </Card>
              </motion.div>
            ))}
          </div>
        </motion.div>
      </div>
    </section>
  );
}
