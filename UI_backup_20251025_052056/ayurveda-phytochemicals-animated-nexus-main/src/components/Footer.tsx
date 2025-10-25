"use client";

import { motion } from "framer-motion";
import { Leaf, Heart, Mail, Github, Twitter, Linkedin } from "lucide-react";

export default function Footer() {
  const socialLinks = [
    { icon: Github, href: "#", label: "GitHub" },
    { icon: Twitter, href: "#", label: "Twitter" },
    { icon: Linkedin, href: "#", label: "LinkedIn" },
  ];

  return (
    <footer className="relative bg-gradient-to-br from-emerald-900 via-teal-900 to-cyan-900 text-white py-16 px-6 overflow-hidden">
      {/* Animated Background */}
      <div className="absolute inset-0 opacity-10">
        {[...Array(10)].map((_, i) => (
          <motion.div
            key={i}
            className="absolute"
            style={{
              left: `${Math.random() * 100}%`,
              top: `${Math.random() * 100}%`,
            }}
            animate={{
              y: [0, -30, 0],
              opacity: [0.2, 0.5, 0.2],
            }}
            transition={{
              duration: 4 + Math.random() * 2,
              repeat: Infinity,
              delay: Math.random() * 2,
            }}
          >
            <Leaf size={40} />
          </motion.div>
        ))}
      </div>

      <div className="max-w-7xl mx-auto relative z-10">
        <div className="grid md:grid-cols-3 gap-12 mb-12">
          {/* Brand Section */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6 }}
          >
            <div className="flex items-center gap-3 mb-4">
              <motion.div
                animate={{ rotate: 360 }}
                transition={{ duration: 8, repeat: Infinity, ease: "linear" }}
              >
                <Leaf size={40} />
              </motion.div>
              <span className="font-cinzel text-3xl font-bold">
                Ayur<span className="text-emerald-300">Science</span>
              </span>
            </div>
            <p className="text-emerald-100 leading-relaxed">
              Bridging the wisdom of ancient Ayurveda with modern phytochemical science for holistic wellness.
            </p>
            <p className="font-devanagari text-xl mt-4 text-emerald-300">
              आयुर्वेद: जीवन का विज्ञान
            </p>
          </motion.div>

          {/* Quick Links */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6, delay: 0.2 }}
          >
            <h3 className="font-cinzel text-xl font-bold mb-4">Quick Links</h3>
            <ul className="space-y-3">
              {["Home", "The Bridge", "Translator", "Timeline", "About Us", "Contact"].map(
                (link, index) => (
                  <motion.li key={link} whileHover={{ x: 5 }}>
                    <a
                      href="#"
                      className="text-emerald-100 hover:text-emerald-300 transition-colors flex items-center gap-2"
                    >
                      <motion.span
                        initial={{ scaleX: 0 }}
                        whileHover={{ scaleX: 1 }}
                        className="w-2 h-2 bg-emerald-300 rounded-full"
                      />
                      {link}
                    </a>
                  </motion.li>
                )
              )}
            </ul>
          </motion.div>

          {/* Contact & Social */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6, delay: 0.4 }}
          >
            <h3 className="font-cinzel text-xl font-bold mb-4">Connect With Us</h3>
            <div className="space-y-4 mb-6">
              <motion.a
                href="mailto:info@ayurscience.com"
                whileHover={{ x: 5 }}
                className="flex items-center gap-3 text-emerald-100 hover:text-emerald-300 transition-colors"
              >
                <Mail size={20} />
                <span>info@ayurscience.com</span>
              </motion.a>
            </div>

            <div className="flex gap-4">
              {socialLinks.map((social, index) => {
                const Icon = social.icon;
                return (
                  <motion.a
                    key={social.label}
                    href={social.href}
                    whileHover={{ scale: 1.2, rotate: 5 }}
                    whileTap={{ scale: 0.9 }}
                    className="w-12 h-12 bg-emerald-800/50 rounded-full flex items-center justify-center hover:bg-emerald-700/50 transition-colors"
                    aria-label={social.label}
                  >
                    <Icon size={20} />
                  </motion.a>
                );
              })}
            </div>
          </motion.div>
        </div>

        {/* Bottom Bar */}
        <motion.div
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.6 }}
          className="pt-8 border-t border-emerald-700/50 flex flex-col md:flex-row justify-between items-center gap-4 text-emerald-200"
        >
          <p className="text-sm">
            © 2024 AyurScience. All rights reserved.
          </p>
          <motion.div
            className="flex items-center gap-2 text-sm"
            whileHover={{ scale: 1.05 }}
          >
            <span>Made with</span>
            <motion.div
              animate={{
                scale: [1, 1.3, 1],
              }}
              transition={{
                duration: 1,
                repeat: Infinity,
                ease: "easeInOut",
              }}
            >
              <Heart size={16} className="text-red-400 fill-red-400" />
            </motion.div>
            <span>for holistic wellness</span>
          </motion.div>
        </motion.div>
      </div>
    </footer>
  );
}
