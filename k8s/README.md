# Kubernetes Lab - Déploiement d'une application Flask avec PostgreSQL

## Description

Ce projet consiste à déployer une application Flask utilisant une base de données PostgreSQL dans un cluster Kubernetes. L'application se connecte à la base de données PostgreSQL et expose deux endpoints API : 
1. `/` pour une page d'accueil simple.
2. `/data` pour récupérer les données depuis la base de données.

Le déploiement est configuré pour être scalable avec plusieurs réplicas et utilise des probes de liveness et readiness pour assurer la disponibilité de l'application.

## Prérequis

- Kubernetes cluster (local ou distant)
- Minikube installé (si tu utilises un cluster local)
- Docker installé pour créer des images locales
- `kubectl` installé et configuré pour interagir avec le cluster Kubernetes

## Étapes pour lancer l'application sur Kubernetes

### 1. Prérequis

Assure-toi d'avoir Kubernetes et Minikube (si nécessaire) configurés.

```bash
# Si tu utilises Minikube, lance un cluster avec 3 nœuds
minikube start --nodes 3 --driver=docker


# Appliquez les manifests Kubernetes :
kubectl apply -f k8s/


# Accédez à l’application via NodePort :

minikube service app-service --url
