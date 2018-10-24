function [fname] = save_img(params, img_info, r, c, dir)
    d = params.d;
    
    fname = '';
    if(r < 1 || r + d > img_info.Height)
        return;
    end
    if(c < 1 || c + d > img_info.Width)
        return;
    end
    
    % read in portion of image
    A = imread(img_info.Filename, 'PixelRegion', {[r, r + d], [c, c + d]});
    fname = sprintf('%s%d_%d.jpg', dir, r, c);

    if(isfield(params, 'resize'))
        A_r = imresize(A, params.resize);
        imwrite(A_r, fname);
    else
        imwrite(A, fname);
    end
end
