import pycuda.autoinit
import pycuda.driver as drv
import numpy as np
from pycuda.compiler import SourceModule
from PIL import Image

def apply_convolution(image_path, kernel):
    image = Image.open(image_path).convert('L')
    image_np = np.array(image).astype(np.float32)
    output_np = np.zeros_like(image_np)

    mod = SourceModule("""
    __global__ void convolution_2d(float *image, float *output, float *kernel, int width, int height, int k_width, int k_height)
    {
        int x = blockIdx.x * blockDim.x + threadIdx.x;
        int y = blockIdx.y * blockDim.y + threadIdx.y;

        if (x >= width || y >= height) return;

        float sum = 0;
        int k_center_x = k_width / 2;
        int k_center_y = k_height / 2;

        for (int j = 0; j < k_height; j++)
        {
            for (int i = 0; i < k_width; i++)
            {
                int x_offset = x + (i - k_center_x);
                int y_offset = y + (j - k_center_y);

                if (x_offset >= 0 && x_offset < width && y_offset >= 0 && y_offset < height)
                {
                    sum += image[y_offset * width + x_offset] * kernel[j * k_width + i];
                }
            }
        }

        output[y * width + x] = sum;
    }
    """)

    convolution_2d = mod.get_function("convolution_2d")

    height, width = image_np.shape
    k_height, k_width = kernel.shape
    image_gpu = drv.mem_alloc(image_np.nbytes)
    output_gpu = drv.mem_alloc(output_np.nbytes)
    kernel_gpu = drv.mem_alloc(kernel.nbytes)

    drv.memcpy_htod(image_gpu, image_np)
    drv.memcpy_htod(output_gpu, output_np)
    drv.memcpy_htod(kernel_gpu, kernel)

    block_size = (16, 16, 1)
    grid_size = (int(np.ceil(width / block_size[0])), int(np.ceil(height / block_size[1])), 1)

    convolution_2d(image_gpu, output_gpu, kernel_gpu, np.int32(width), np.int32(height), np.int32(k_width), np.int32(k_height), block=block_size, grid=grid_size)

    drv.memcpy_dtoh(output_np, output_gpu)

    output_image = Image.fromarray(output_np.astype(np.uint8))
    output_image_path = image_path.replace(".jpg", "_filtered.jpg")
    output_image.save(output_image_path)

    return output_image_path
