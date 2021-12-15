# Helm chart

This chart deploys an API with `Deployment`, `Service`, `Ingress` on a Kubernetes cluster using the Helm package manager.

## Installing Helm chart:

> #### helm install my-release-name -f values.yaml (location of the values.yaml found) -n namespace

To install the chart with the release name `my-release`:
```
helm install test-helm -f values.yaml . -n namespace
```
The command deploys the chart on the Kubernetes cluster in the specified namespace(optional). 

&nbsp;

## Upgrading Helm chart:

> #### helm upgrade my-release-name -f values.yaml (location of the values.yaml found) -n namespace

To update the chart with the release name `my-release`:
```
helm upgrade test-helm -f values.yaml . -n namespace
```
The command upgrades the chart on the Kubernetes cluster in the specified namespace(optional). 

&nbsp;

## Uninstalling Helm chart:

> #### helm uninstall my-release-name -n namespace

To uninstall the chart with the release name `my-release`:
```
helm uninstall test-helm -n namespace
```
The command removes all the Kubernetes components associated with the chart and deletes the release.

&nbsp;

## List Helm release:

> #### helm ls -n namespace
To list the helm releases in the specified namespace: 
```
helm ls -n namespace
```

