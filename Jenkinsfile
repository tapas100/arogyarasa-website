pipeline {
    agent any
    stages {
        stage("Checkout") {
            steps { checkout scm }
        }
        stage("Setup") {
            steps { sh "python3 -m pip install --quiet beautifulsoup4" }
        }
        stage("Visual Hierarchy") {
            steps { sh "python3 scripts/visual_hierarchy.py frontend/src/app/page.tsx > hierarchy.json"; archiveArtifacts artifacts: "hierarchy.json", fingerprint: true }
        }
        stage("Analyze Other Repos") {
            steps { sh "./ci/analyze_other_repos.sh" }
        }
    }
    post { always { echo "CI pipeline completed" } }
}
