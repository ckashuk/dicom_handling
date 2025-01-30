import glob
import numpy as np
import SimpleITK as sitk
from matplotlib import pyplot as plt

from dcm.loaders import load_dicom_series_sitk
from dcm.regridder import generate_regridded_image, generate_grid, generate_regridded_volume

dcm_root = '//onfnas01.uwhis.hosp.wisc.edu/radiology/Groups/GarrettGroup/Research/ProstateSPORE/DODDatasetComplete/CleanedProject/prosspore/DODProjectRead'
pet_dcm_root = f'{dcm_root}/17009_pyl17/PET1/PET AC Prostate/dicom'
mr_dcm_root = f'{dcm_root}/17009_pyl17/PET1/Obl Axial T2 Prostate/dicom'

pet, _, _ = load_dicom_series_sitk(pet_dcm_root)
mr, _, _ = load_dicom_series_sitk(mr_dcm_root)
print("loaded!")
pet_grid = generate_grid(mr)
print("gridded!")
# proj0 = generate_regridded_volume(mr, pet_grid)
# print("projected0!", np.min(proj0), np.mean(proj0), np.max(proj0))
proj1 = generate_regridded_volume(mr, pet_grid, mode=sitk.sitkLinear)
print("projected1!", np.min(proj1), np.mean(proj1), np.max(proj1))
proj2 = generate_regridded_volume(mr, pet_grid, mode=sitk.sitkNearestNeighbor)
print("projected2!", np.min(proj2), np.mean(proj2), np.max(proj2))
# proj3 = generate_regridded_volume(mr, pet_grid, mode=sitk.sitkBSplineResampler)
# print("projected3!", np.min(proj3), np.mean(proj3), np.max(proj3))

plt.plot(proj1[:, :, :, :], proj2[:, :, :, :])
plt.show()

"""
diff12 = proj1-proj2
diff13 = proj1-proj3
diff23 = proj2-proj3

for diff in [diff12, diff13, diff23]:
    print(np.min(diff), np.mean(diff), np.std(diff), np.max(diff))

bins = range(0, 5000, 10)
hist1 = np.histogram(proj1, bins)
hist2 = np.histogram(proj2, bins)
hist3 = np.histogram(proj3, bins)
plt.plot(hist1[1][0:-1], hist1[0])
plt.plot(hist2[1][0:-1], hist2[0])
plt.plot(hist3[1][0:-1], hist3[0])
plt.show()
"""