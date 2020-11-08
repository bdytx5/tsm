import os
import glob
import sys
import cv2
import shutil

import argparse
out_path = ''

count = 0
def dump_frames(vid_path,num_of_videos):
# def dump_frames(vid_path):
    # video = cv2.VideoCapture(vid_path)
    # vid_name = vid_path.split('/')[-1].split('.')[0]
    # out_full_path = os.path.join(out_path, vid_name)

    # fcount = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    # try:
    #     os.mkdir(out_full_path)
    # except OSError:
    #     pass

    # file_list = []
    # for i in range(fcount):
    #     ret, frame = video.read()
    #     try:
    #         assert ret
    #     except Exception as e:
    #         print('Frame number', i)
    #         print('Total number of frames', fcount)
    
    #     cv2.imwrite('{}/{:06d}.jpg'.format(out_full_path, i), frame)
    #     access_path = '{}/{:06d}.jpg'.format(vid_name, i)
    #     file_list.append(access_path)

    # print('{} done'.format(vid_name))
    # sys.stdout.flush()










    # return file_list
    video = cv2.VideoCapture(vid_path)
    vid_name = vid_path.split('/')[-1].split('.')[0]
    out_full_path = os.path.join(out_path, vid_name)

    fcount = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    try:
        os.mkdir(out_full_path)
    except OSError:
        pass
    file_list = []
    print(fcount)

    for i in list(range(fcount - 1)):
        (ret, frame) = video.read()
        if not ret:
            try:
                shutil.rmtree(out_full_path)
                break
            except:
                break
        #resizedFrame = frame #cv2.resize(frame, (64, 64))
        # assert ret, 'Err: {} - {}'.format(vid_name, i)
        cv2.imwrite('{}/img_{:05d}.jpg'.format(out_full_path, i+1), frame)
        access_path = '{}/img_{:05d}.jpg'.format(vid_name, i+1)
        file_list.append(access_path)
    global count 
    count = count + 1
    print ('--> {}/{} -> {} done'.format(count,num_of_videos,vid_name))
    sys.stdout.flush()
    return file_list

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="extract frames from videos")
    parser.add_argument("src_dir")
    parser.add_argument("out_dir")
    parser.add_argument("--ext", type=str, default='avi', choices=['avi','mp4'], help='video file extensions')

    args = parser.parse_args()

    # out_path = args.out_dir
    # src_path = args.src_dir
    # ext = args.ext

    # if not os.path.isdir(out_path):
    #     print("creating folder: "+out_path)
    #     os.makedirs(out_path)
    # print(src_path+'/*/*.'+ext)

    # vid_list = glob.glob(src_path+'/*/*.'+ext)
    # print('Number of videos',len(vid_list))

    # file_list = list(map(dump_frames, vid_list))
    # # file_list = dump_frames(src_path+'/TrampolineJumping/v_TrampolineJumping_g06_c02.avi')


    # file_list_file_path = os.path.join(out_path, 'file_list.txt')
    # with open(file_list_file_path, 'w') as f:
    #     f.write(str(file_list))

    



    out_path = args.out_dir
    src_path = args.src_dir
    ext = args.ext
    #count = 0

    if not os.path.isdir(out_path):
        print ('creating folder: ' + out_path)
        os.makedirs(out_path)

    vid_list = glob.glob(src_path + '/*/*.' + ext)
    print ('total number of videos found: ', len(vid_list))

    try:
        os.mkdir(out_path)
    except OSError:
        pass

    for vid in vid_list:
        dump_frames(vid,len(vid_list))