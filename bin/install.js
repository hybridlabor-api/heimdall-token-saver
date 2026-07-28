#!/usr/bin/env node
const { spawnSync } = require('child_process');
const path = require('path');

const installScript = path.join(__dirname, '..', 'install.py');
const result = spawnSync('python3', [installScript, '--target', 'both'], { stdio: 'inherit' });
process.exit(result.status || 0);
