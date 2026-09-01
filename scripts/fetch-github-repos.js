#!/usr/bin/env node
// Récupère des repos GitHub par mot-clé via l'API de recherche et sauvegarde en JSON.

const https = require('https');
const fs = require('fs');
const path = require('path');

const QUERIES = ['Caveman', 'Task observer'];
const OUTPUT_FILE = path.join(__dirname, '..', 'github-repos.json');

function searchRepos(query) {
  return new Promise((resolve, reject) => {
    const url = `https://api.github.com/search/repositories?q=${encodeURIComponent(query + ' in:name')}&sort=stars&order=desc&per_page=10`;
    https.get(url, { headers: { 'User-Agent': 'cyberskills-ecc-fetch-repos' } }, (res) => {
      let data = '';
      res.on('data', (chunk) => (data += chunk));
      res.on('end', () => {
        if (res.statusCode !== 200) {
          reject(new Error(`GitHub API error ${res.statusCode} for query "${query}": ${data}`));
          return;
        }
        try {
          const json = JSON.parse(data);
          resolve(
            json.items.map((r) => ({
              name: r.name,
              full_name: r.full_name,
              url: r.html_url,
              description: r.description,
              stars: r.stargazers_count,
              language: r.language,
              updated_at: r.updated_at,
            }))
          );
        } catch (err) {
          reject(err);
        }
      });
    }).on('error', reject);
  });
}

async function main() {
  const results = {};
  for (const query of QUERIES) {
    console.log(`Recherche: ${query}`);
    results[query] = await searchRepos(query);
  }
  fs.writeFileSync(OUTPUT_FILE, JSON.stringify(results, null, 2));
  console.log(`Résultats sauvegardés dans ${OUTPUT_FILE}`);
}

main().catch((err) => {
  console.error(err.message);
  process.exit(1);
});
