"use client";

import { motion, useScroll, useTransform } from "framer-motion";
import { useRef } from "react";
import { Card } from "@/components/ui/card";
import { BookOpen, Microscope, Dna, Globe, Sparkles } from "lucide-react";

interface TimelineEvent {
  year: string;
  title: string;
  description: string;
  icon: any;
  color: string;
}

const timelineData: TimelineEvent[] = [
  {
    year: "5000 BCE",
    title: "Birth of Ayurveda",
    description: "Ancient sages document healing knowledge in the Vedas, establishing the foundation of holistic medicine.",
    icon: BookOpen,
    color: "from-amber-500 to-orange-600",
  },
  {
    year: "1500 BCE",
    title: "Charaka Samhita",
    description: "Comprehensive compilation of Ayurvedic principles, including plant-based remedies and their properties.",
    icon: BookOpen,
    color: "from-orange-500 to-red-600",
  },
  {
    year: "1800s",
    title: "Dawn of Chemistry",
    description: "Scientists begin isolating active compounds from plants, marking the birth of phytochemistry.",
    icon: Microscope,
    color: "from-green-500 to-emerald-600",
  },
  {
    year: "1950s",
    title: "Modern Research",
    description: "Advanced analytical techniques reveal the molecular mechanisms of traditional herbs.",
    icon: Dna,
    color: "from-blue-500 to-cyan-600",
  },
  {
    year: "2000s",
    title: "Scientific Validation",
    description: "Clinical trials confirm efficacy of Ayurvedic compounds, bridging ancient wisdom with evidence-based medicine.",
    icon: Globe,
    color: "from-purple-500 to-pink-600",
  },
  {
    year: "Today",
    title: "Integrated Medicine",
    description: "Global acceptance of phytochemicals as complementary medicine, revolutionizing healthcare worldwide.",
    icon: Sparkles,
    color: "from-indigo-500 to-violet-600",
  },
];

export default function Timeline() {
  const containerRef = useRef<HTMLDivElement>(null);
  const { scrollYProgress } = useScroll({
    target: containerRef,
    offset: ["start end", "end start"],
  });

  return (
    <section
      ref={containerRef}
      className="py-24 px-6 bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-50 dark:from-slate-950 dark:via-blue-950 dark:to-indigo-950 relative overflow-hidden"
    >
      {/* Animated Background */}
      <div className="absolute inset-0 opacity-20">
        {[...Array(15)].map((_, i) => (
          <motion.div
            key={i}
            className="absolute w-2 h-2 bg-primary rounded-full"
            style={{
              left: `${Math.random() * 100}%`,
              top: `${Math.random() * 100}%`,
            }}
            animate={{
              y: [0, -50, 0],
              opacity: [0.2, 1, 0.2],
            }}
            transition={{
              duration: 3 + Math.random() * 2,
              repeat: Infinity,
              delay: Math.random() * 2,
            }}
          />
        ))}
      </div>

      <div className="max-w-6xl mx-auto relative z-10">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8 }}
          className="text-center mb-20"
        >
          <h2 className="font-cinzel text-4xl md:text-5xl font-bold mb-6 text-foreground">
            Journey Through Time
          </h2>
          <p className="text-xl text-muted-foreground max-w-3xl mx-auto">
            From ancient Vedic wisdom to modern molecular science
          </p>
        </motion.div>

        {/* Timeline */}
        <div className="relative">
          {/* Central Line */}
          <motion.div
            className="absolute left-1/2 transform -translate-x-1/2 w-1 bg-gradient-to-b from-primary via-accent to-secondary h-full hidden md:block"
            style={{
              scaleY: useTransform(scrollYProgress, [0, 1], [0, 1]),
              transformOrigin: "top",
            }}
          />

          {/* Timeline Events */}
          <div className="space-y-24">
            {timelineData.map((event, index) => {
              const isEven = index % 2 === 0;
              const Icon = event.icon;

              return (
                <motion.div
                  key={index}
                  initial={{ opacity: 0, x: isEven ? -100 : 100 }}
                  whileInView={{ opacity: 1, x: 0 }}
                  viewport={{ once: true, margin: "-100px" }}
                  transition={{ duration: 0.8, delay: 0.2 }}
                  className={`flex items-center gap-8 ${
                    isEven ? "md:flex-row" : "md:flex-row-reverse"
                  } flex-col`}
                >
                  {/* Content Card */}
                  <motion.div
                    whileHover={{ scale: 1.05, rotateY: isEven ? 5 : -5 }}
                    className="w-full md:w-5/12"
                  >
                    <Card className="p-6 backdrop-blur-sm bg-card/90 border-2 border-primary/20 hover:border-primary/50 transition-all shadow-xl hover:shadow-2xl">
                      <div className="flex items-start gap-4">
                        <motion.div
                          animate={{
                            rotate: [0, 360],
                            scale: [1, 1.2, 1],
                          }}
                          transition={{
                            duration: 4,
                            repeat: Infinity,
                            ease: "easeInOut",
                          }}
                          className={`p-3 rounded-full bg-gradient-to-br ${event.color} shadow-lg`}
                        >
                          <Icon className="text-white" size={24} />
                        </motion.div>
                        <div className="flex-1">
                          <motion.div
                            className={`inline-block px-3 py-1 rounded-full bg-gradient-to-r ${event.color} text-white text-sm font-bold mb-3`}
                            whileHover={{ scale: 1.1 }}
                          >
                            {event.year}
                          </motion.div>
                          <h3 className="font-cinzel text-2xl font-bold mb-3 text-foreground">
                            {event.title}
                          </h3>
                          <p className="text-muted-foreground leading-relaxed">
                            {event.description}
                          </p>
                        </div>
                      </div>
                    </Card>
                  </motion.div>

                  {/* Center Circle */}
                  <motion.div
                    initial={{ scale: 0 }}
                    whileInView={{ scale: 1 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.5, delay: 0.4 }}
                    className="hidden md:flex w-16 h-16 rounded-full bg-gradient-to-br from-primary to-accent shadow-lg items-center justify-center relative z-10"
                  >
                    <motion.div
                      animate={{
                        scale: [1, 1.5, 1],
                        opacity: [1, 0, 1],
                      }}
                      transition={{
                        duration: 2,
                        repeat: Infinity,
                        ease: "easeInOut",
                      }}
                      className="absolute inset-0 rounded-full bg-primary"
                    />
                    <motion.div
                      animate={{ rotate: 360 }}
                      transition={{
                        duration: 8,
                        repeat: Infinity,
                        ease: "linear",
                      }}
                      className="relative z-10"
                    >
                      <Icon className="text-white" size={28} />
                    </motion.div>
                  </motion.div>

                  {/* Spacer */}
                  <div className="w-full md:w-5/12" />
                </motion.div>
              );
            })}
          </div>
        </div>

        {/* Bottom Decoration */}
        <motion.div
          initial={{ opacity: 0, scale: 0.8 }}
          whileInView={{ opacity: 1, scale: 1 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8, delay: 0.4 }}
          className="mt-20 text-center"
        >
          <div className="inline-block p-8 rounded-full bg-gradient-to-br from-primary/20 to-accent/20 backdrop-blur-sm">
            <motion.div
              animate={{ rotate: 360 }}
              transition={{ duration: 10, repeat: Infinity, ease: "linear" }}
            >
              <Sparkles size={60} className="text-primary" />
            </motion.div>
          </div>
        </motion.div>
      </div>
    </section>
  );
}
