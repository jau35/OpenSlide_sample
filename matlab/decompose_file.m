function [dir] = decompose_file(params)
    % required params
    filename = params.filename;
    n = params.n;
    d = params.d;
    
    % optional params
    out_dir = './';
    r_begin = 1;
    c_begin = 1;
    
    if(isfield(params, 'out_dir'))
        out_dir = params.out_dir;
    end
    if(isfield(params, 'r_begin'))
        r_begin = params.r_begin;
    end
    if(isfield(params, 'c_begin'))
        c_begin = params.c_begin;
    end
    
    r_end = r_begin + (n-1)*d;
    c_end = c_begin + (n-1)*d;
    
    % get file info
    info = imfinfo(filename);
    img_info = info(1)
    
    % create output directory
    [path, file] = fileparts(img_info.Filename);
    dir = sprintf('%s/%s/%d/', out_dir, file, d);
    mkdir(dir);
    
    % save images
    for r = r_begin:d:r_end
        for c = c_begin:d:c_end
            if(strcmp(save_img(params, r, c, img_info.Height, img_info.Width, dir), ''))
                fprintf('Failed: r=%d, c=%d\n', r, c);
            end
        end
    end
end

