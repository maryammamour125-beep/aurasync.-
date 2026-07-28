import React, { useState } from 'react';
import {
  StyleSheet,
  Text,
  View,
  SafeAreaView,
  TouchableOpacity,
  ScrollView,
  TextInput,
  Switch,
} from 'react-native';

// Static Archetype Data
const ARCHETYPES = {
  noir: {
    name: 'The Noir Detective',
    tagline: 'Deliberate, cynical, and observant.',
    quest: 'Order your coffee using concise, minimal phrasing. Observe three details about a stranger today.',
    props: ['Tortoiseshell glasses', 'Leather folio or notebook', 'Neutral-toned trench or coat'],
  },
  minimalist: {
    name: 'The Minimalist Architect',
    tagline: 'Clean lines, purposeful spaces, absolute clarity.',
    quest: 'Clear your physical workspace of all non-essential items before starting your work.',
    props: ['Monochrome watch', 'Plain black or white notebook', 'Fountain pen'],
  },
  journalist: {
    name: 'The 1970s Journalist',
    tagline: 'Inquisitive, fast-paced, relentless truth-seeker.',
    quest: 'Ask three deep, open-ended questions in conversations today instead of small talk.',
    props: ['Vintage messenger bag', 'Portable tape recorder or voice memo app ready', 'Corduroy or textured jacket'],
  },
};

export default function App() {
  const [selectedKey, setSelectedKey] = useState(null);
  const [questDone, setQuestDone] = useState(false);
  const [reflection, setReflection] = useState('');
  const [submitted, setSubmitted] = useState(false);

  const activeArchetype = selectedKey ? ARCHETYPES[selectedKey] : null;

  // Reset state to change archetype
  const handleReset = () => {
    setSelectedKey(null);
    setQuestDone(false);
    setReflection('');
    setSubmitted(false);
  };

  // --- SCREEN 1: ARCHETYPE SELECTION ---
  if (!selectedKey) {
    return (
      <SafeAreaView style={styles.container}>
        <View style={styles.headerContainer}>
          <Text style={styles.title}>THE METHOD</Text>
          <Text style={styles.subtitle}>Select your persona to begin transmission.</Text>
        </View>

        <ScrollView contentContainerStyle={styles.scrollContainer}>
          {Object.keys(ARCHETYPES).map((key) => {
            const item = ARCHETYPES[key];
            return (
              <TouchableOpacity
                key={key}
                style={styles.card}
                onPress={() => setSelectedKey(key)}
              >
                <Text style={styles.cardTitle}>{item.name}</Text>
                <Text style={styles.cardTagline}>{item.tagline}</Text>
              </TouchableOpacity>
            );
          })}
        </ScrollView>
      </SafeAreaView>
    );
  }

  // --- SCREEN 2: MAIN DASHBOARD & REFLECTION ---
  return (
    <SafeAreaView style={styles.container}>
      <ScrollView contentContainerStyle={styles.scrollContainer}>
        {/* Header / Active Persona */}
        <View style={styles.activeHeader}>
          <View>
            <Text style={styles.activePreText}>ACTIVE ARCHETYPE</Text>
            <Text style={styles.activeTitle}>{activeArchetype.name}</Text>
          </View>
          <TouchableOpacity onPress={handleReset} style={styles.switchButton}>
            <Text style={styles.switchButtonText}>Switch</Text>
          </TouchableOpacity>
        </View>

        {/* Daily Scene Quest */}
        <View style={styles.sectionCard}>
          <Text style={styles.sectionTitle}>TODAY'S SCENE QUEST</Text>
          <Text style={styles.questText}>{activeArchetype.quest}</Text>
          
          <View style={styles.rowBetween}>
            <Text style={styles.label}>Mark Quest Complete</Text>
            <Switch
              value={questDone}
              onValueChange={setQuestDone}
              trackColor={{ false: '#333', true: '#fff' }}
              thumbColor={questDone ? '#000' : '#888'}
            />
          </View>
        </View>

        {/* Capsule Checklist */}
        <View style={styles.sectionCard}>
          <Text style={styles.sectionTitle}>PROP & WARDROBE CHECKLIST</Text>
          {activeArchetype.props.map((prop, index) => (
            <View key={index} style={styles.propRow}>
              <Text style={styles.bullet}>•</Text>
              <Text style={styles.propText}>{prop}</Text>
            </View>
          ))}
        </View>

        {/* End of Day Reflection */}
        <View style={styles.sectionCard}>
          <Text style={styles.sectionTitle}>END OF DAY REFLECTION</Text>
          <TextInput
            style={styles.textInput}
            placeholder="How did you embody the character today? Where did you break?"
            placeholderTextColor="#666"
            multiline
            value={reflection}
            onChangeText={setReflection}
          />
          <TouchableOpacity
            style={[styles.submitButton, submitted && styles.submittedButton]}
            onPress={() => setSubmitted(true)}
          >
            <Text style={styles.submitButtonText}>
              {submitted ? 'Transmission Logged ✓' : 'Log Daily Performance'}
            </Text>
          </TouchableOpacity>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

// --- STYLES ---
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0a0a0a',
  },
  headerContainer: {
    padding: 24,
    borderBottomWidth: 1,
    borderBottomColor: '#222',
  },
  title: {
    fontSize: 24,
    fontWeight: '900',
    color: '#ffffff',
    letterSpacing: 3,
  },
  subtitle: {
    fontSize: 14,
    color: '#888',
    marginTop: 4,
  },
  scrollContainer: {
    padding: 20,
  },
  card: {
    backgroundColor: '#161616',
    borderWidth: 1,
    borderColor: '#333',
    padding: 20,
    borderRadius: 8,
    marginBottom: 16,
  },
  cardTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 6,
  },
  cardTagline: {
    fontSize: 14,
    color: '#aaa',
  },
  activeHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 20,
    paddingBottom: 16,
    borderBottomWidth: 1,
    borderBottomColor: '#222',
  },
  activePreText: {
    fontSize: 10,
    color: '#666',
    letterSpacing: 2,
    marginBottom: 2,
  },
  activeTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#fff',
  },
  switchButton: {
    backgroundColor: '#222',
    paddingVertical: 8,
    paddingHorizontal: 14,
    borderRadius: 6,
  },
  switchButtonText: {
    color: '#ccc',
    fontSize: 12,
    fontWeight: '600',
  },
  sectionCard: {
    backgroundColor: '#141414',
    borderWidth: 1,
    borderColor: '#262626',
    borderRadius: 8,
    padding: 16,
    marginBottom: 16,
  },
  sectionTitle: {
    fontSize: 11,
    fontWeight: 'bold',
    color: '#888',
    letterSpacing: 1.5,
    marginBottom: 12,
  },
  questText: {
    fontSize: 15,
    color: '#eee',
    lineHeight: 22,
    marginBottom: 16,
  },
  rowBetween: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    borderTopWidth: 1,
    borderTopColor: '#222',
    paddingTop: 12,
  },
  label: {
    fontSize: 14,
    color: '#ccc',
  },
  propRow: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 8,
  },
  bullet: {
    color: '#888',
    marginRight: 8,
    fontSize: 16,
  },
  propText: {
    fontSize: 14,
    color: '#ddd',
  },
  textInput: {
    backgroundColor: '#1c1c1c',
    color: '#fff',
    padding: 12,
    borderRadius: 6,
    height: 90,
    textAlignVertical: 'top',
    fontSize: 14,
    marginBottom: 12,
    borderWidth: 1,
    borderColor: '#333',
  },
  submitButton: {
    backgroundColor: '#fff',
    padding: 12,
    borderRadius: 6,
    alignItems: 'center',
  },
  submittedButton: {
    backgroundColor: '#2e7d32',
  },
  submitButtonText: {
    color: '#000',
    fontWeight: 'bold',
    fontSize: 13,
    letterSpacing: 1,
  },
});
