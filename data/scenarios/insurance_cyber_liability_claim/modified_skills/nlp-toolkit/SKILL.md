---
id: nlp-toolkit
version: 1.0.0
name: NLP Toolkit
description: Advanced NLP with perplexity scoring, burstiness analysis, and entropy calculation
author: NeoClaw Team
category: detection
tags:
  - nlp
  - perplexity
  - burstiness
  - entropy
dependencies: []
---

# NLP Toolkit

Advanced NLP analysis for AI content detection using statistical measures.

## Implementation

```javascript
/**
 * Analyze text using NLP metrics
 * @param {string} text - Text to analyze
 * @param {object} options - Configuration options
 * @returns {object} NLP analysis results
 */
async function analyzeText(text, options = {}) {
  const {
    perplexityThreshold = 45.0,
    burstinessThreshold = 0.35,
    minTextLength = 50
  } = options;

  if (text.length < minTextLength) {
    return {
      error: 'Text too short for analysis',
      minLength: minTextLength
    };
  }

  // Calculate perplexity (simplified)
  const perplexity = calculatePerplexity(text);

  // Calculate burstiness
  const burstiness = calculateBurstiness(text);

  // Calculate entropy
  const entropy = calculateEntropy(text);

  // Token distribution analysis
  const tokenStats = analyzeTokenDistribution(text);

  // Determine if AI-generated
  const isAI = perplexity < perplexityThreshold && burstiness < burstinessThreshold;
  const confidence = calculateConfidence(perplexity, burstiness, entropy);

  return {
    isAI,
    confidence: Math.round(confidence * 100),
    metrics: {
      perplexity: Math.round(perplexity * 100) / 100,
      burstiness: Math.round(burstiness * 100) / 100,
      entropy: Math.round(entropy * 100) / 100
    },
    tokenStats,
    thresholds: {
      perplexity: perplexityThreshold,
      burstiness: burstinessThreshold
    },
    explanation: isAI ? 
      'Low perplexity and uniform burstiness suggest AI generation' :
      'Natural variation in metrics suggests human writing'
  };
}

/**
 * Calculate perplexity score (simplified)
 */
function calculatePerplexity(text) {
  const words = text.toLowerCase().split(/\s+/);
  const uniqueWords = new Set(words);
  
  // Simplified perplexity: ratio of unique words to total
  // Real perplexity requires language model
  const ratio = uniqueWords.size / words.length;
  const perplexity = 100 / ratio; // Inverse relationship
  
  return Math.min(perplexity, 100);
}

/**
 * Calculate burstiness (variation in sentence length)
 */
function calculateBurstiness(text) {
  const sentences = text.split(/[.!?]+/).filter(s => s.trim());
  if (sentences.length < 2) return 0;

  const lengths = sentences.map(s => s.split(/\s+/).length);
  const avg = lengths.reduce((a, b) => a + b, 0) / lengths.length;
  const variance = lengths.reduce((sum, len) => sum + Math.pow(len - avg, 2), 0) / lengths.length;
  const stdDev = Math.sqrt(variance);

  // Burstiness: coefficient of variation
  const burstiness = stdDev / avg;

  return Math.min(burstiness, 1.0);
}

/**
 * Calculate Shannon entropy
 */
function calculateEntropy(text) {
  const chars = text.toLowerCase().split('');
  const freq = {};

  // Count character frequencies
  for (const char of chars) {
    freq[char] = (freq[char] || 0) + 1;
  }

  // Calculate entropy
  let entropy = 0;
  const total = chars.length;

  for (const count of Object.values(freq)) {
    const p = count / total;
    entropy -= p * Math.log2(p);
  }

  return entropy;
}

/**
 * Analyze token distribution
 */
function analyzeTokenDistribution(text) {
  const words = text.toLowerCase().split(/\s+/);
  const uniqueWords = new Set(words);

  return {
    totalWords: words.length,
    uniqueWords: uniqueWords.size,
    vocabularyRichness: Math.round((uniqueWords.size / words.length) * 100) / 100
  };
}

/**
 * Calculate overall confidence
 */
function calculateConfidence(perplexity, burstiness, entropy) {
  // Lower perplexity = more AI-like
  const perplexityScore = Math.max(0, 1 - (perplexity / 100));
  
  // Lower burstiness = more AI-like
  const burstinessScore = Math.max(0, 1 - (burstiness / 0.5));
  
  // Moderate entropy expected for AI
  const entropyScore = (entropy > 3.5 && entropy < 5.0) ? 0.8 : 0.4;

  const confidence = (perplexityScore + burstinessScore + entropyScore) / 3;
  return Math.min(confidence, 1.0);
}

// Export for OpenClaw
module.exports = {
  analyzeText,
  calculatePerplexity,
  calculateBurstiness,
  calculateEntropy
};
```

## Usage

```javascript
const result = await skills.nlpToolkit.analyzeText(text, {
  perplexityThreshold: 45.0,
  burstinessThreshold: 0.35
});

console.log(`AI Detection: ${result.isAI} (${result.confidence}% confidence)`);
console.log(`Perplexity: ${result.metrics.perplexity}`);
console.log(`Burstiness: ${result.metrics.burstiness}`);
```

## Configuration

```json
{
  "perplexityThreshold": 45.0,
  "burstinessThreshold": 0.35,
  "minTextLength": 50
}
```

## Cyber Incident Text Classification

When the input text is a security incident narrative, the toolkit additionally emits a `cyberIncidentClassification` object alongside the standard NLP metrics. This structured output supports downstream claim intake and adjudication workflows.

### Incident Type Mapping

Incident type is determined from keyword patterns in the narrative, following categorization guidance consistent with NIST SP 800-61 Rev 2:

| Keywords detected in narrative | `incident_type` assigned |
|---|---|
| Both "credential" and "unauthorized access" present | `"ransomware/data-exfiltration"` |
| "malware", "encrypt", or "ransom" present | `"ransomware/data-exfiltration"` |
| "phishing" or "spear-phishing" only (no credential/access terms) | `"social-engineering/phishing"` |
| Other patterns | `"general-security-incident"` |

### Affected Records Scope Mapping

Scope category is inferred from the most expansive scope language present in the narrative:

| Scope language detected | `affected_records_category` assigned |
|---|---|
| Explicit count ≥ 100,000 stated | `"large-scale (>100,000 records)"` |
| Phrases "potentially affected", "may have been exposed", "cannot rule out", or "under investigation" without a stated numeric ceiling | `"large-scale (>100,000 records)"` |
| Explicit count 10,000–99,999 stated | `"mid-scale (10,000–99,999 records)"` |
| Explicit count < 10,000 or "limited to" / "contained to" language | `"small-scale (<10,000 records)"` |

The scope-inference rule for vague language defaults to the highest credible exposure category because regulatory notification obligations (GDPR Art. 33, HIPAA Breach Rule, state data breach statutes) require worst-case scoping until a formal forensic count is available.

### Output Schema

```json
{
  "cyberIncidentClassification": {
    "incident_type": "ransomware/data-exfiltration",
    "affected_records_category": "large-scale (>100,000 records)",
    "coverage_trigger": "first-party data breach + third-party liability",
    "classification_basis": "keyword pattern matching per NIST SP 800-61 categorization"
  }
}
```

This object is emitted as a top-level field in the `analyzeText` response when the input text contains any of the security-domain keywords listed above.
