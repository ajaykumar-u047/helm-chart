# Tilt 

### To install Tilt in MACOS/Linux

```
curl -fsSL https://raw.githubusercontent.com/tilt-dev/tilt/master/scripts/install.sh | bash
```

&nbsp;

### Tiltfile

//cfg variable which reads the tilt_config.json where k8s context and docker container registry info are stored.
> cfg = read_json('tilt_config.json')

> k8s_yaml(['k8.yaml','k8_service.yaml'])

> k8s_resource('test-deployment', port_forwards=5001)

//Replace the cluster context where you have to deploy
> allow_k8s_contexts(cfg['K8S_CONTEXT'])

//Container registry to sync images from ...
> docker_build(cfg['CONTAINER_REGISTRY'], '.', build_args={})

can be added in tilt_config.json 
//"CONTAINER_REGISTRY": "dockertesting047/flask-calc:1.0.0"

### To run the tilt

``` 
tilt up
```

### To stop/remove the k8s components

```
tilt down
```