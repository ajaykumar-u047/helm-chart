cfg = read_json('tilt_config.json')

k8s_yaml(['k8.yaml','k8_service.yaml'])
# k8s_resource('test-deployment', port_forwards=5001)

# Replace the cluster context where you have to deploy
allow_k8s_contexts(cfg['K8S_CONTEXT'])

# Container registry to sync images from ...
# docker_build(cfg['CONTAINER_REGISTRY'], '.', build_args={})
