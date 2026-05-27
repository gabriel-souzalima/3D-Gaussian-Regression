import torch

def build_cholesky_matrix(params):

    L = torch.zeros(size = (params.shape[0],3,3),
                    dtype = params.dtype,
                    device = params.device) 
    L[:,0,0] = params[:,0]
    L[:,1,1] = params[:,1]
    L[:,2,2] = params[:,2]
    L[:,1,0] = params[:,3]
    L[:,2,0] = params[:,4]
    L[:,2,1] = params[:,5]
    return L 
cholesky_matrix = build_cholesky_matrix(params)
print(cholesky_matrix)

def sigma_from_cholesky(cholesky_matrix):
   covariance_matrix = cholesky_matrix @ cholesky_matrix.transpose(1,2)
   return covariance_matrix


def standardOBB_2_Gauss(obb_info)

    xyz = obb_info(:, :3)
    
# tests:
"""params = torch.tensor([[2.0,3.0,4.0,1.0,0.5,0.2],[2.0,3.0,4.0,1.0,0.5,0.2],[2.0,3.0,4.0,1.0,0.5,0.2],[2.0,3.0,4.0,1.0,0.5,0.2]])
obb_info = torch.tensor([[2.0,3.0,4.0,1.0,0.5,0.2,20.0]])
cholesky_matrix = build_cholesky_matrix(params)
print(cholesky_matrix)
covariance_matrix = sigma_from_cholesky(cholesky_matrix)
print(covariance_matrix)""" 


