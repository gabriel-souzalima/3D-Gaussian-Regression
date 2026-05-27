# Gaussian Regression for 3D Object Detection

Based on [MMDetection3D](https://github.com/open-mmlab/mmdetection3d) 

## Install

```bash
# MMDetection3D must be installed
python3 -c "import mmdet3d; print(mmdet3d.__version__)"

# Install Gauss3D
pip install -e . --user
```

## Use

```bash
# Train baseline pointpillars
python tools/train.py configs_gaucho3d/pointpillars/baseline_kitti_car.py

# Train Gauss3D
python tools/train.py configs_gaucho3d/pointpillars/gaussian_pointpillars_kitti_car.py
```

## References

- [GauCho](https://github.com/jhlmarques/GauCho) — CVPR 2025
- [MMDetection3D](https://github.com/open-mmlab/mmdetection3d)
- [PointPillars](https://arxiv.org/abs/1812.05784)


