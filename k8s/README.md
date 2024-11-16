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


# Vérifiez si les pods s'exécutent avec la commande :

kubectl get pods
# Pour afficher plus de détails sur un pod spécifique ou connaître les raisons de son état actuel, utilisez :

kubectl describe pod <nom-du-pod>

# Remplacez <nom-du-pod> par le nom du pod que vous souhaitez examiner.

Cette commande est utile pour déboguer les problèmes liés aux pods.

## Accéder à l'application
# Affichez tous les services avec la commande suivante :

kubectl get services

# Lorsqu'un service Kubernetes est configuré avec NodePort, vous pouvez y accéder facilement en exécutant :

minikube service <nom-du-service> --url
# Remplacez <nom-du-service> par le nom du service que vous souhaitez accéder. Cette commande génère une URL temporaire que # vous pouvez utiliser dans votre navigateur pour tester ou interagir avec le service.

# Vous pouvez également établir une connexion entre votre machine locale et un pod pour tester l'API. Utilisez la commande # suivante :

kubectl port-forward <nom-du-pod> 5000:5000

# Remplacez <nom-du-pod> par le nom du pod auquel vous souhaitez accéder.
# Remarque : Le port 5000 est celui sur lequel l'API est exposée


