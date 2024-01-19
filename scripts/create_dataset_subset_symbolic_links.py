import argparse
import os
import random

SAMPLING_METHOD_RANDOM = 'sampling-random'
SAMPLING_METHOD_RANDOM_FIXED_SEED = 'sampling-random-fixed-seed'
SAMPLING_METHOD_SORTED = 'sampling-sorted'
SAMPLING_METHOD_SORTED_REVERSE = 'sampling-sorted-reverse'

SUPPORTED_SAMPLING_METHODS = [
    SAMPLING_METHOD_RANDOM,
    SAMPLING_METHOD_RANDOM_FIXED_SEED,
    SAMPLING_METHOD_SORTED,
    SAMPLING_METHOD_SORTED_REVERSE
]


def main():
    parser = argparse.ArgumentParser(description="Create subset of dataset with symbolic links")
    parser.add_argument('--input-folder', type=str, required=True, help='Path to input folder')
    parser.add_argument('--output-folder', type=str, required=True, default='', help='Path to output folder with symbolic links')
    parser.add_argument('--max-samples-class', type=int, required=True, help='Max samples per class')
    parser.add_argument('--sampling-method', type=str, required=False, default=SAMPLING_METHOD_RANDOM_FIXED_SEED,
                        help='Sampling method of subset. Supported methods are: {}'.format(SUPPORTED_SAMPLING_METHODS))
    parser.add_argument('--random-seed', type=int, required=False, default=0, help='Random seed')

    args = parser.parse_args()

    if args.sampling_method not in SUPPORTED_SAMPLING_METHODS:
        raise ValueError('Sampling method {} not supported. Supported ones are {}.'.format(args.sampling_method,
                                                                                           SUPPORTED_SAMPLING_METHODS))

    class_folders = [x for x in os.listdir(args.input_folder) if os.path.isdir(os.path.join(args.input_folder, x))]

    os.mkdir(args.output_folder)

    for class_folder in class_folders:
        input_class_path = os.path.join(args.input_folder, class_folder)
        output_class_path = os.path.join(args.output_folder, class_folder)

        os.mkdir(output_class_path)

        class_image_files = [x for x in os.listdir(input_class_path) if os.path.isfile(os.path.join(input_class_path, x))]

        if args.sampling_method == SAMPLING_METHOD_RANDOM:
            class_image_files = sorted(class_image_files)
            random.shuffle(class_image_files)
        elif args.sampling_method == SAMPLING_METHOD_RANDOM_FIXED_SEED:
            class_image_files = sorted(class_image_files)
            random.Random(args.random_seed).shuffle(class_image_files)
        elif args.sampling_method == SAMPLING_METHOD_SORTED_REVERSE:
            class_image_files = sorted(class_image_files, reverse=True)
        elif args.sampling_method == SAMPLING_METHOD_SORTED:
            class_image_files = sorted(class_image_files)

        if len(class_image_files) > args.max_samples_class:
            class_image_files = class_image_files[0:args.max_samples_class]

        for image_file in class_image_files:
            os.symlink(os.path.join(input_class_path, image_file), os.path.join(output_class_path, image_file))

    print('Finished creating symlinks')


if __name__ == "__main__":
    main()
