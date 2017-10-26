USE mavcooksite;


INSERT INTO Project (title, date, isfeatured, description, thumbnail, project_seq, type) VALUES
    ('Code-M Logo Design', '2016-07-01', 0, 
        'I designed this logo for the Code-M student organization at the University of Michigan. 
        Currently I am on the board for Code-M as the Media Chair, and this was one of my first 
        projects as such. I wanted the logo to represent what Code-M is about: connecting students 
        at U of M who are interested in learning about computer science. The \'M\' is an 
        artistic rendering of a tree data structure that symbolizes growth and connections.<br><br>
        The logo has a floating color scheme, so the colors can change depending on the need. 
        This is useful for providing associations with different types of events.', 
        'media/projects/thumbnails/codem_med.jpg', 
        1, 'STD'),
    
    ('Front and Central Graphics', '2013-01-01', 0, 
        'This is the open from the graphic design package I made for my high school video 
        broadcasting class. So I designed the theme music, 
        logo, lower thirds, transitions, and some other bumpers for the show. 
        My graphics package was used on the show from 2013-2016.', 
        'media/projects/thumbnails/frontCentral_med.jpg', 3, 'STD'),
    
    ('Java Menu', '2016-02-10', 0, 
        'This video showcases a piece of a larger application I worked on for a public display application 
        in the CYGNSS mission headquarters.
        This menu selection system I wrote, in Java, is the user control interface, so people can control 
        the parent application via keypad.
        In the full application, the thumbnails, 
        labels, and descriptions are passed from the parent app.
        <br><br>The menu can work as a standalone 
        application, that can pull in text for the description area, and scales the font to fit. 
        The number of menu items can be updated with the change of a variable, and the program 
        detects when the slide out bars need to slide left so they appear on the screen.', 
        'media/projects/thumbnails/cygnss_med.jpg', 8, 'STD'),
    
    ('Wall-E Model', '2011-06-01', 1, 
        'This is a 3D model of Pixar\'s Wall-E I made in June 2011. I modeled, animated, and lit these scenes 
        in Cinema 4D. According to my notes, this only took six hours to model and light. Since it was
        made so quickly, the model doesn\'t have great topology and isn\'t rigged. The animation 
        was done quickly just to show off the model, not to showcase animation skills.', 
        'media/projects/thumbnails/walle_med.jpg', 6, 'STD'),
    
    ('TCFF Volunteer Video', '2014-03-01', 0, 
        'I made this animation as a volunteer of the Travese City Film Festival (TCFF). The 
        purpose of the animation was to introduce a video thanking 
        other TCFF volunteers. Videos of the venues were provided by the TCFF.
        <br><br>
        This was a fun project because I got to meet some cool people, tried out
        a new motion-graphics style, and I had TCFF branding requirements (which was new for me).', 
        'media/projects/thumbnails/tcff_med.jpg', 5, 'STD'),
    
    ('Demo Reel', '2012-12-01', 0, 
        'This is an old demo reel of mine. The first video is a more flashy version of a demo reel, since it focuses more 
        on editing than showing each piece of work all the way through. Sorry about the music, it was the best royalty 
        free music I could find in 2012.', 
        'media/projects/thumbnails/dr2012_med.jpg', 7, 'STD'),
    
    ('Mavcook.com', '2016-06-01', 0, 
        'This is my personal website that I initially made just to teach myself HTML, CSS, and a bit of JavaScript. 
        I tried to do everything from the ground up, no HTML or CSS frameworks. I even made all the icons (minus the company ones like Github and Youtube).
        After I finished the basic site, I still wanted to add more, so I learned PHP and MySQL to add the 
        additional ideas I had.
        <br><br>
        In an effort to make the code nicer and more maintainable, I transitioned the site over to use Python Flask.',
        'media/projects/thumbnails/mavcook.com.jpg', 9, 'STD'),

    ('Photography', '2014-01-01', 0, 
        'Just some pictures I have taken that I enjoy.',
        'media/projects/thumbnails/photogal.jpg', 2, 'GAL'),

    ('Digital Art', '2010-01-01', 0, 
        'Some computer art I have made.',
        'media/projects/thumbnails/digiart.jpg', 4, 'GAL'),

    ('LivLy', '2017-02-13', 0, 
        'This is a Google Chrome extension I made that replaces your New Tab page. I made this for a specific person, and they used an extension for a new tab page that had a really obnoxious clock that covered the nice backgrounds they had, and that annoyed me for some reason. So I decided I would make something for them with a good design, was minimal, and still provided shortcuts to their favorite sites. I also added some compliments to help them get through the day.<br><br>If it sounds like something you would enjoy using, check it out here:<br><a href="https://chrome.google.com/webstore/detail/livly/jodlifhapikdhppocniogknenmjlaiog">Download</a><br><br><a href="https://github.com/mavcook/LivLy">Source</a>',
        'media/projects/thumbnails/livly.jpg', 0, 'STD')
;


INSERT INTO PTags (name) VALUES
    ('Graphic Design'),
    ('Motion Graphics'),
    ('Programming'),
    ('3D Art'),
    ('Video Editing'),
    ('Animation')
;

INSERT INTO TagsToProject(project_id, ptag_id) VALUES
    (1, 1),
    (2, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 2),
    (5, 5),
    (6, 5),
    (6, 2),
    (6, 4),
    (7, 1),
    (7, 3),
    (9, 1),
    (9, 4),
    (9, 6),
    (10, 1),
    (10, 3)
;



INSERT INTO Media (project_id, directoryPath) VALUES
    (1, 'media/projects/codem'),
    (2, 'media/projects/frontCentral'),
    (3, 'media/projects/cygnss'),
    (4, 'media/projects/walle'),
    (5, 'media/projects/tcff'),
    (6, 'media/projects/dr2012'),
    (7, 'media/projects/mavcook.com'),
    (8, 'media/projects/photogal'),
    (8, 'media/projects/thumbnails/photogal'),
    (9, 'media/projects/digiart'),    
    (9, 'media/projects/thumbnails/digiart'),
    (10, 'media/projects/livly')
;
