"use client";

import { motion, AnimatePresence } from "framer-motion";
import { useState } from "react";
import { Card } from "@/components/ui/card";
import { Textarea } from "@/components/ui/textarea";
import { Button } from "@/components/ui/button";
import { 
  Sparkles, 
  Leaf, 
  FlaskConical, 
  Brain, 
  Loader2,
  ArrowRight,
  CheckCircle2,
  AlertCircle
} from "lucide-react";
import { analyzeText, getDemoData, type AnalysisResult } from "@/lib/api";
import { useToast } from "@/hooks/use-toast";

export default function AnalysisInterface() {
  const [text, setText] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<AnalysisResult | null>(null);
  const [error, setError] = useState<string | null>(null);
  const { toast } = useToast();

  const handleAnalyze = async () => {
    if (!text.trim()) {
      toast({
        title: "Please enter some text",
        description: "Enter Ayurvedic text to analyze",
        variant: "destructive",
      });
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const data = await analyzeText(text);
      setResult(data);
      toast({
        title: "Analysis Complete!",
        description: `Found ${data.herbs.length} herbs and ${data.hypotheses.length} hypotheses`,
      });
    } catch (err) {
      setError(err instanceof Error ? err.message : "Analysis failed");
      toast({
        title: "Analysis Failed",
        description: "Please try again or check if the backend is running",
        variant: "destructive",
      });
    } finally {
      setLoading(false);
    }
  };

  const handleDemo = async () => {
    setLoading(true);
    setError(null);

    try {
      const data = await getDemoData();
      setResult(data);
      setText("Turmeric (Curcuma longa) combined with black pepper (Piper nigrum) enhances bioavailability. The hot property of these herbs aids in digestion and reduces inflammation.");
      toast({
        title: "Demo Data Loaded!",
        description: "Explore the analysis results below",
      });
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to load demo");
      toast({
        title: "Demo Failed",
        description: "Please check if the backend is running",
        variant: "destructive",
      });
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="py-24 px-6 bg-gradient-to-br from-purple-50 via-pink-50 to-rose-50 dark:from-purple-950 dark:via-pink-950 dark:to-rose-950 relative overflow-hidden">
      {/* Animated Background */}
      <div className="absolute inset-0 overflow-hidden pointer-events-none">
        {[...Array(15)].map((_, i) => (
          <motion.div
            key={i}
            className="absolute rounded-full bg-gradient-to-br from-primary/10 to-accent/10"
            style={{
              left: `${Math.random() * 100}%`,
              top: `${Math.random() * 100}%`,
              width: `${Math.random() * 300 + 100}px`,
              height: `${Math.random() * 300 + 100}px`,
            }}
            animate={{
              scale: [1, 1.2, 1],
              opacity: [0.1, 0.3, 0.1],
              x: [0, Math.random() * 100 - 50, 0],
              y: [0, Math.random() * 100 - 50, 0],
            }}
            transition={{
              duration: 10 + Math.random() * 10,
              repeat: Infinity,
              ease: "easeInOut",
              delay: Math.random() * 5,
            }}
          />
        ))}
      </div>

      <div className="max-w-7xl mx-auto relative z-10">
        {/* Header */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8 }}
          className="text-center mb-12"
        >
          <motion.div
            animate={{
              rotate: [0, 360],
            }}
            transition={{ duration: 20, repeat: Infinity, ease: "linear" }}
            className="inline-block mb-6"
          >
            <Brain size={60} className="text-primary" />
          </motion.div>
          <h2 className="font-cinzel text-4xl md:text-5xl font-bold mb-4 bg-gradient-to-r from-purple-600 via-pink-600 to-rose-600 dark:from-purple-400 dark:via-pink-400 dark:to-rose-400 bg-clip-text text-transparent">
            AI-Powered Ayurvedic Analysis
          </h2>
          <p className="text-xl text-muted-foreground max-w-3xl mx-auto">
            Extract herbs, properties, and modern compounds from ancient texts
          </p>
        </motion.div>

        {/* Input Section */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8, delay: 0.2 }}
        >
          <Card className="p-8 backdrop-blur-lg bg-card/90 border-2 border-primary/20 shadow-2xl">
            <div className="space-y-6">
              <Textarea
                placeholder="Enter Ayurvedic text here... (e.g., 'Turmeric has bitter taste and hot potency')"
                value={text}
                onChange={(e) => setText(e.target.value)}
                className="min-h-[200px] text-lg resize-none bg-background/50 backdrop-blur-sm border-2 border-primary/20 focus:border-primary/50 transition-all"
              />
              
              <div className="flex flex-wrap gap-4 justify-center">
                <motion.div whileHover={{ scale: 1.05 }} whileTap={{ scale: 0.95 }}>
                  <Button
                    onClick={handleAnalyze}
                    disabled={loading || !text.trim()}
                    size="lg"
                    className="px-8 py-6 text-lg bg-gradient-to-r from-primary to-accent hover:shadow-xl transition-all"
                  >
                    {loading ? (
                      <>
                        <Loader2 className="mr-2 animate-spin" size={24} />
                        Analyzing...
                      </>
                    ) : (
                      <>
                        <Sparkles className="mr-2" size={24} />
                        Analyze Text
                      </>
                    )}
                  </Button>
                </motion.div>

                <motion.div whileHover={{ scale: 1.05 }} whileTap={{ scale: 0.95 }}>
                  <Button
                    onClick={handleDemo}
                    disabled={loading}
                    size="lg"
                    variant="outline"
                    className="px-8 py-6 text-lg border-2 border-primary hover:bg-primary/10 transition-all"
                  >
                    Try Demo
                  </Button>
                </motion.div>
              </div>
            </div>
          </Card>
        </motion.div>

        {/* Error State */}
        <AnimatePresence>
          {error && (
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -20 }}
              className="mt-8"
            >
              <Card className="p-6 bg-destructive/10 border-2 border-destructive/50">
                <div className="flex items-center gap-3">
                  <AlertCircle className="text-destructive" size={32} />
                  <div>
                    <h3 className="font-semibold text-lg">Analysis Error</h3>
                    <p className="text-muted-foreground">{error}</p>
                  </div>
                </div>
              </Card>
            </motion.div>
          )}
        </AnimatePresence>

        {/* Results Section */}
        <AnimatePresence>
          {result && (
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              className="mt-12 space-y-8"
            >
              {/* Herbs Found */}
              <motion.div
                initial={{ opacity: 0, x: -50 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ duration: 0.6, delay: 0.1 }}
              >
                <Card className="p-8 backdrop-blur-lg bg-card/90 border-2 border-primary/30 shadow-xl overflow-hidden relative">
                  <motion.div
                    className="absolute top-0 right-0 w-64 h-64 bg-gradient-to-bl from-primary/20 to-transparent rounded-full blur-3xl"
                    animate={{
                      scale: [1, 1.2, 1],
                      opacity: [0.3, 0.5, 0.3],
                    }}
                    transition={{ duration: 4, repeat: Infinity }}
                  />
                  
                  <div className="relative z-10">
                    <div className="flex items-center gap-3 mb-6">
                      <motion.div
                        animate={{ rotate: [0, 360] }}
                        transition={{ duration: 8, repeat: Infinity, ease: "linear" }}
                      >
                        <Leaf className="text-primary" size={40} />
                      </motion.div>
                      <h3 className="font-cinzel text-3xl font-bold">Herbs Identified</h3>
                    </div>
                    
                    <div className="flex flex-wrap gap-3">
                      {result.herbs.map((herb, index) => (
                        <motion.div
                          key={herb}
                          initial={{ opacity: 0, scale: 0.8 }}
                          animate={{ opacity: 1, scale: 1 }}
                          transition={{ delay: index * 0.1 }}
                          whileHover={{ scale: 1.1, rotate: [0, -5, 5, 0] }}
                        >
                          <div className="px-6 py-3 bg-gradient-to-r from-primary/20 to-accent/20 border-2 border-primary/30 rounded-full font-semibold text-lg backdrop-blur-sm">
                            {herb}
                          </div>
                        </motion.div>
                      ))}
                    </div>
                  </div>
                </Card>
              </motion.div>

              {/* Ayurvedic Properties */}
              {Object.keys(result.ayurvedic_properties).length > 0 && (
                <motion.div
                  initial={{ opacity: 0, x: 50 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ duration: 0.6, delay: 0.2 }}
                >
                  <Card className="p-8 backdrop-blur-lg bg-card/90 border-2 border-accent/30 shadow-xl">
                    <div className="flex items-center gap-3 mb-6">
                      <Sparkles className="text-accent" size={40} />
                      <h3 className="font-cinzel text-3xl font-bold">Ayurvedic Properties</h3>
                    </div>
                    
                    <div className="grid md:grid-cols-2 gap-6">
                      {Object.entries(result.ayurvedic_properties).map(([herb, props], index) => (
                        <motion.div
                          key={herb}
                          initial={{ opacity: 0, y: 30 }}
                          animate={{ opacity: 1, y: 0 }}
                          transition={{ delay: index * 0.15 }}
                          whileHover={{ scale: 1.02 }}
                        >
                          <Card className="p-6 bg-gradient-to-br from-background/50 to-accent/5 border-2 border-accent/20 hover:border-accent/40 transition-all">
                            <h4 className="font-bold text-xl mb-4 text-primary">{herb}</h4>
                            <div className="space-y-2">
                              {Object.entries(props).map(([key, value]) => (
                                <div key={key} className="flex justify-between items-center">
                                  <span className="text-muted-foreground capitalize">{key}:</span>
                                  <span className="font-semibold">
                                    {Array.isArray(value) ? value.join(", ") : value}
                                  </span>
                                </div>
                              ))}
                            </div>
                          </Card>
                        </motion.div>
                      ))}
                    </div>
                  </Card>
                </motion.div>
              )}

              {/* Modern Compounds */}
              {Object.keys(result.modern_compounds).length > 0 && (
                <motion.div
                  initial={{ opacity: 0, x: -50 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ duration: 0.6, delay: 0.3 }}
                >
                  <Card className="p-8 backdrop-blur-lg bg-card/90 border-2 border-primary/30 shadow-xl">
                    <div className="flex items-center gap-3 mb-6">
                      <motion.div
                        animate={{ scale: [1, 1.2, 1] }}
                        transition={{ duration: 2, repeat: Infinity }}
                      >
                        <FlaskConical className="text-primary" size={40} />
                      </motion.div>
                      <h3 className="font-cinzel text-3xl font-bold">Modern Compounds</h3>
                    </div>
                    
                    <div className="space-y-6">
                      {Object.entries(result.modern_compounds).map(([herb, compounds], herbIndex) => (
                        <motion.div
                          key={herb}
                          initial={{ opacity: 0, y: 30 }}
                          animate={{ opacity: 1, y: 0 }}
                          transition={{ delay: herbIndex * 0.15 }}
                        >
                          <h4 className="font-bold text-xl mb-3 text-accent">{herb}</h4>
                          <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-4">
                            {compounds.map((compound, compIndex) => (
                              <motion.div
                                key={compIndex}
                                initial={{ opacity: 0, scale: 0.9 }}
                                animate={{ opacity: 1, scale: 1 }}
                                transition={{ delay: (herbIndex * 0.15) + (compIndex * 0.05) }}
                                whileHover={{ scale: 1.05, rotate: [0, 2, -2, 0] }}
                              >
                                <Card className="p-4 bg-gradient-to-br from-primary/10 to-accent/10 border border-primary/20 hover:border-primary/40 transition-all">
                                  <p className="font-semibold text-lg mb-2">{compound.name}</p>
                                  {compound.molecular_formula && (
                                    <p className="text-sm text-muted-foreground font-mono">
                                      {compound.molecular_formula}
                                    </p>
                                  )}
                                  {compound.molecular_weight && (
                                    <p className="text-xs text-muted-foreground mt-1">
                                      MW: {compound.molecular_weight}
                                    </p>
                                  )}
                                </Card>
                              </motion.div>
                            ))}
                          </div>
                        </motion.div>
                      ))}
                    </div>
                  </Card>
                </motion.div>
              )}

              {/* Hypotheses */}
              {result.hypotheses.length > 0 && (
                <motion.div
                  initial={{ opacity: 0, y: 50 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.6, delay: 0.4 }}
                >
                  <Card className="p-8 backdrop-blur-lg bg-gradient-to-br from-card/90 to-primary/5 border-2 border-primary/40 shadow-2xl">
                    <div className="flex items-center gap-3 mb-6">
                      <motion.div
                        animate={{
                          rotate: [0, 360],
                        }}
                        transition={{ duration: 15, repeat: Infinity, ease: "linear" }}
                      >
                        <Brain className="text-primary" size={40} />
                      </motion.div>
                      <h3 className="font-cinzel text-3xl font-bold">AI-Generated Hypotheses</h3>
                    </div>
                    
                    <div className="space-y-4">
                      {result.hypotheses.map((hypothesis, index) => (
                        <motion.div
                          key={index}
                          initial={{ opacity: 0, x: -30 }}
                          animate={{ opacity: 1, x: 0 }}
                          transition={{ delay: 0.4 + (index * 0.1) }}
                          whileHover={{ scale: 1.02, x: 10 }}
                        >
                          <Card className="p-6 bg-gradient-to-r from-background/80 to-primary/10 border-l-4 border-primary hover:border-accent transition-all">
                            <div className="flex items-start gap-4">
                              <motion.div
                                initial={{ scale: 0 }}
                                animate={{ scale: 1 }}
                                transition={{ delay: 0.5 + (index * 0.1), type: "spring" }}
                              >
                                <CheckCircle2 className="text-primary mt-1" size={24} />
                              </motion.div>
                              <div className="flex-1">
                                <div className="flex items-center gap-2 mb-3">
                                  <span className="px-3 py-1 bg-primary/20 rounded-full text-sm font-semibold">
                                    {hypothesis.herb}
                                  </span>
                                  <ArrowRight className="text-accent" size={20} />
                                  <span className="px-3 py-1 bg-accent/20 rounded-full text-sm font-semibold">
                                    {hypothesis.compound}
                                  </span>
                                </div>
                                <p className="text-lg mb-2">
                                  <span className="font-semibold text-primary">{hypothesis.ayurvedic_property}</span>
                                  {" correlates with "}
                                  <span className="font-semibold text-accent">{hypothesis.correlation}</span>
                                </p>
                                {hypothesis.confidence && (
                                  <p className="text-sm text-muted-foreground">
                                    Confidence: {hypothesis.confidence}
                                  </p>
                                )}
                              </div>
                            </div>
                          </Card>
                        </motion.div>
                      ))}
                    </div>
                  </Card>
                </motion.div>
              )}
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    </section>
  );
}
