# Tilt 

Tilt is a cloud-native development engine for teams that deploy to Kubernetes. It enables developers to test code changes easily and get feedback. Tilt listens to code changes, builds images, and deploys them in Kubernetes. Subsequent changes are reflected instantly with the help of its live sync features. 

### To install Tilt in MACOS/Linux

```
curl -fsSL https://raw.githubusercontent.com/tilt-dev/tilt/master/scripts/install.sh | bash
```

&nbsp;

## Tiltfile

read_json functions tells the tilt engine to read and store the json in variable cfg.
```
cfg = read_json('tilt_config.json')
```
k8s_yaml function tells tilt which Kubernetes objects need deploying and calling k8s_resource is used here to configure port forwarding for the k8s resource.
```
k8s_yaml(['k8.yaml','k8_service.yaml'])
```
```
k8s_resource('test-deployment', port_forwards=5001)
```
Specifies that Tilt is allowed to run against the specified k8s context names. By default, Tilt automatically allows Minikube, Docker for Desktop, Microk8s and so on. As I am using remote Kubernetes dev cluster I am allowing cluster context explicitly to reduce chances of deploying it to some other cluster that is not intended.
```
allow_k8s_contexts(cfg['K8S_CONTEXT'])
```

Container registry to sync images from ...
```
docker_build(cfg['CONTAINER_REGISTRY'], '.', build_args={})
```
can be added in tilt_config.json 
```
"CONTAINER_REGISTRY": "dockertesting047/flask-calc:1.0.0"
```

## To run tilt:

``` 
tilt up
```

## To stop/remove the resources from Tilt and Kubernetes:

```
tilt down
```
