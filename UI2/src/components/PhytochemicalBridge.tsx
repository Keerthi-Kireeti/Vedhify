"use client";

import { motion } from "framer-motion";
import { useState } from "react";
import { Card } from "@/components/ui/card";
import { Leaf, FlaskConical, ArrowRight } from "lucide-react";

interface HerbCompound {
  herb: string;
  sanskrit: string;
  compound: string;
  benefit: string;
  color: string;
}

const herbData: HerbCompound[] = [
  {
    herb: "Turmeric",
    sanskrit: "हरिद्रा (Haridra)",
    compound: "Curcumin",
    benefit: "Anti-inflammatory & Antioxidant",
    color: "from-yellow-400 to-orange-500",
  },
  {
    herb: "Ashwagandha",
    sanskrit: "अश्वगंधा",
    compound: "Withanolides",
    benefit: "Adaptogenic & Stress Relief",
    color: "from-green-400 to-emerald-600",
  },
  {
    herb: "Tulsi",
    sanskrit: "तुलसी",
    compound: "Eugenol & Ursolic Acid",
    benefit: "Immune Booster & Antimicrobial",
    color: "from-lime-400 to-green-600",
  },
  {
    herb: "Brahmi",
    sanskrit: "ब्राह्मी",
    compound: "Bacosides",
    benefit: "Cognitive Enhancement",
    color: "from-cyan-400 to-blue-600",
  },
  {
    herb: "Neem",
    sanskrit: "नीम",
    compound: "Azadirachtin",
    benefit: "Antibacterial & Detoxifying",
    color: "from-teal-400 to-green-700",
  },
  {
    herb: "Triphala",
    sanskrit: "त्रिफला",
    compound: "Tannins & Polyphenols",
    benefit: "Digestive Health",
    color: "from-amber-400 to-orange-600",
  },
];

export default function PhytochemicalBridge() {
  const [hoveredIndex, setHoveredIndex] = useState<number | null>(null);

  return (
    <section className="py-24 px-6 bg-gradient-to-br from-emerald-50 via-teal-50 to-cyan-50 dark:from-emerald-950 dark:via-teal-950 dark:to-cyan-950 relative overflow-hidden">
      {/* Background Animation */}
      <div className="absolute inset-0 opacity-10">
        {[...Array(20)].map((_, i) => (
          <motion.div
            key={i}
            className="absolute w-32 h-32 border border-primary rounded-full"
            style={{
              left: `${Math.random() * 100}%`,
              top: `${Math.random() * 100}%`,
            }}
            animate={{
              scale: [1, 1.5, 1],
              opacity: [0.1, 0.3, 0.1],
            }}
            transition={{
              duration: 5 + Math.random() * 3,
              repeat: Infinity,
              delay: Math.random() * 2,
            }}
          />
        ))}
      </div>

      <div className="max-w-7xl mx-auto relative z-10">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8 }}
          className="text-center mb-16"
        >
          <div className="flex justify-center items-center gap-4 mb-6">
            <motion.div
              animate={{ rotate: [0, 360] }}
              transition={{ duration: 8, repeat: Infinity, ease: "linear" }}
            >
              <Leaf size={50} className="text-primary" />
            </motion.div>
            <motion.div
              animate={{ x: [0, 10, 0] }}
              transition={{ duration: 2, repeat: Infinity }}
            >
              <ArrowRight size={40} className="text-accent" />
            </motion.div>
            <motion.div
              animate={{ scale: [1, 1.2, 1] }}
              transition={{ duration: 2, repeat: Infinity }}
            >
              <FlaskConical size={50} className="text-accent" />
            </motion.div>
          </div>
          <h2 className="font-cinzel text-4xl md:text-5xl font-bold mb-6 text-foreground">
            The Phytochemical Bridge
          </h2>
          <p className="text-xl text-muted-foreground max-w-3xl mx-auto">
            Discover how ancient Ayurvedic herbs contain powerful modern compounds
          </p>
        </motion.div>

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {herbData.map((item, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 50 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6, delay: index * 0.1 }}
              onHoverStart={() => setHoveredIndex(index)}
              onHoverEnd={() => setHoveredIndex(null)}
            >
              <motion.div
                whileHover={{ scale: 1.05, rotateY: 5 }}
                className="h-full"
              >
                <Card className="relative overflow-hidden h-full backdrop-blur-sm bg-card/90 border-2 border-primary/20 hover:border-primary/50 transition-all shadow-xl hover:shadow-2xl">
                  {/* Gradient Overlay */}
                  <motion.div
                    className={`absolute inset-0 bg-gradient-to-br ${item.color} opacity-0`}
                    animate={{
                      opacity: hoveredIndex === index ? 0.1 : 0,
                    }}
                    transition={{ duration: 0.3 }}
                  />

                  <div className="relative z-10 p-6">
                    {/* Herb Section */}
                    <motion.div
                      animate={{
                        y: hoveredIndex === index ? -5 : 0,
                      }}
                      transition={{ duration: 0.3 }}
                      className="mb-6"
                    >
                      <div className="flex items-center gap-3 mb-3">
                        <motion.div
                          animate={{
                            rotate: hoveredIndex === index ? 360 : 0,
                          }}
                          transition={{ duration: 0.6 }}
                        >
                          <Leaf className="text-primary" size={32} />
                        </motion.div>
                        <div>
                          <h3 className="font-cinzel text-2xl font-bold text-foreground">
                            {item.herb}
                          </h3>
                          <p className="font-devanagari text-sm text-primary">
                            {item.sanskrit}
                          </p>
                        </div>
                      </div>
                    </motion.div>

                    {/* Arrow Connector */}
                    <motion.div
                      animate={{
                        x: hoveredIndex === index ? [0, 10, 0] : 0,
                      }}
                      transition={{
                        duration: 1,
                        repeat: hoveredIndex === index ? Infinity : 0,
                      }}
                      className="flex justify-center my-4"
                    >
                      <ArrowRight className="text-accent" size={32} />
                    </motion.div>

                    {/* Compound Section */}
                    <motion.div
                      animate={{
                        y: hoveredIndex === index ? 5 : 0,
                      }}
                      transition={{ duration: 0.3 }}
                      className="mb-6"
                    >
                      <div className="flex items-center gap-3 mb-3">
                        <motion.div
                          animate={{
                            scale: hoveredIndex === index ? [1, 1.2, 1] : 1,
                          }}
                          transition={{
                            duration: 0.8,
                            repeat: hoveredIndex === index ? Infinity : 0,
                          }}
                        >
                          <FlaskConical className="text-accent" size={32} />
                        </motion.div>
                        <div>
                          <h4 className="text-xl font-bold text-accent">
                            {item.compound}
                          </h4>
                          <p className="text-xs text-muted-foreground">
                            Active Phytochemical
                          </p>
                        </div>
                      </div>
                    </motion.div>

                    {/* Benefit */}
                    <motion.div
                      animate={{
                        opacity: hoveredIndex === index ? 1 : 0.7,
                      }}
                      className="p-4 bg-muted/50 rounded-lg border border-primary/20"
                    >
                      <p className="text-sm font-semibold text-center">
                        {item.benefit}
                      </p>
                    </motion.div>
                  </div>

                  {/* Decorative Corner */}
                  <motion.div
                    className="absolute top-0 right-0 w-20 h-20 bg-gradient-to-bl from-primary/20 to-transparent"
                    animate={{
                      scale: hoveredIndex === index ? 1.5 : 1,
                      opacity: hoveredIndex === index ? 1 : 0.5,
                    }}
                  />
                </Card>
              </motion.div>
            </motion.div>
          ))}
        </div>

        {/* Bottom CTA */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8, delay: 0.6 }}
          className="mt-16 text-center"
        >
          <motion.button
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            className="px-8 py-4 bg-primary text-primary-foreground rounded-full font-semibold text-lg shadow-lg hover:shadow-xl transition-all"
          >
            Explore More Connections
          </motion.button>
        </motion.div>
      </div>
    </section>
  );
}
