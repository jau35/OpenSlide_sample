function [fname] = save_img(params, r, c, H, W, dir)
    d = params.d;
    
    fname = '';
    if(r < 1 || r + d > H)
        return;
    end
    if(c < 1 || c + d > W)
        return;
    end
    
    % read in portion of image
    A = imread(params.filename, 'PixelRegion', {[r, r + d], [c, c + d]});
    fname = sprintf('%s%d_%d.jpg', dir, r, c);

    if(isfield(params, 'resize'))
        A_r = imresize(A, params.resize);
        imwrite(A_r, fname);
    else
        imwrite(A, fname);
    end
end
