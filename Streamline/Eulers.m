
im = imread('pic.PNG');
im = flipud(im);



hax = gca; %get the axis handle
image([-20,20],[-14,14],im); %plot the image within the axis limits
hold on; %enable plotting overwrite

filename = 'FixedTimeSlow.xlsx';
data = readtable(filename);
[rows, columns] = size(data);
cnt=1;
for col = 1 : 2 : columns
    x = data{1:rows, col};
    X = rmmissing(x);
    y = data{1:rows, col + 1};
    Y = rmmissing(y);
    plot(X, Y, "r");
    cnt=cnt+1;
    hold on;
end
axis equal;
