// Minimal passthrough loader referenced by next.config.ts
module.exports = function componentTaggerLoader(source) {
  // This loader is intentionally a noop for now. It returns the source unchanged.
  // Add tagging logic here if you later need to process component sources.
  return source;
};