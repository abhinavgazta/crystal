package com.mygdx.game;

/**
 * Created by abhinavgazta on 8/14/16.
 */

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Input;
import com.badlogic.gdx.Screen;
import com.badlogic.gdx.audio.Music;
import com.badlogic.gdx.audio.Sound;
import com.badlogic.gdx.graphics.GL20;
import com.badlogic.gdx.graphics.OrthographicCamera;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.math.MathUtils;
import com.badlogic.gdx.math.Rectangle;
import com.badlogic.gdx.math.Vector3;
import com.badlogic.gdx.physics.box2d.Body;
import com.badlogic.gdx.scenes.scene2d.ui.Image;
import com.badlogic.gdx.utils.Array;
import com.badlogic.gdx.utils.TimeUtils;

import java.util.Iterator;



public class GameScreenLevelTwo implements Screen {
    final DropLevelTwo game;
    Texture dropImage;
    Texture dropImageRed;
    Texture bucketImage;
    Sound dropSound;
    Music rainMusic;
    OrthographicCamera camera;
    Rectangle bucket;
    Rectangle bottom;
    Array<Rectangle> raindrops;
    Array<Rectangle> redRainDrops;
    long lastDropTime;
    long lastRedDropTime;
    int dropsGathered;
    Body bodyEdgeScreen;


    public GameScreenLevelTwo(final DropLevelTwo gam) {
        this.game = gam;

        // load the images for the droplet and the bucket, 64x64 pixels each
        dropImage = new Texture(Gdx.files.internal("droplet.png"));
        dropImageRed = new Texture(Gdx.files.internal("dropletred.png"));
        bucketImage = new Texture(Gdx.files.internal("bucket.png"));

        // load the drop sound effect and the rain background "music"
        dropSound = Gdx.audio.newSound(Gdx.files.internal("drop.wav"));
        rainMusic = Gdx.audio.newMusic(Gdx.files.internal("rain.mp3"));
        rainMusic.setLooping(true);

        // create the camera and the SpriteBatch
        camera = new OrthographicCamera();
        camera.setToOrtho(false, 800, 480);

        // create a Rectangle to logically represent the bucket
        bucket = new Rectangle();
        bottom = new Rectangle();
        bucket.x = 800 / 2 - 64 / 2; // center the bucket horizontally
        bucket.y = 20; // bottom left corner of the bucket is 20 pixels above
        // the bottom screen edge
        bucket.width = 64;
        bucket.height = 64;

        // create the raindrops array and spawn the first raindrop
        raindrops = new Array<Rectangle>();
        redRainDrops = new Array<Rectangle>();
        spawnRaindrop();
        //spawnRaindropRed();


    }

    private void spawnRaindrop() {
        Rectangle raindrop = new Rectangle();
        raindrop.x = MathUtils.random(0, 800 - 64);
        raindrop.y = 480;
        raindrop.width = 64;
        raindrop.height = 64;
        raindrops.add(raindrop);
        lastDropTime = TimeUtils.nanoTime();
    }

    private void spawnRaindropRed() {
        Rectangle raindrop = new Rectangle();
        raindrop.x = MathUtils.random(0, 800 - 64);
        raindrop.y = 430;
        raindrop.width = 64;
        raindrop.height = 64;
        redRainDrops.add(raindrop);
        lastRedDropTime = TimeUtils.millis();
    }

    @Override
    public void render(float delta) {
        // clear the screen with a dark blue color. The
        // arguments to glClearColor are the red, green
        // blue and alpha component in the range [0,1]
        // of the color to be used to clear the screen.
        Gdx.gl.glClearColor(0, 0, 0.2f, 1);
        Gdx.gl.glClear(GL20.GL_COLOR_BUFFER_BIT);

        // tell the camera to update its matrices.
        camera.update();

        // tell the SpriteBatch to render in the
        // coordinate system specified by the camera.
        game.batch.setProjectionMatrix(camera.combined);
        // begin a new batch and draw the bucket and
        // all drops
        game.batch.begin();
        game.font.draw(game.batch, "Total Drops Collected: " + dropsGathered, 10, 480);
        game.font.draw(game.batch, "Collect Total 1000: ", 450, 480);
        game.batch.draw(bucketImage, bucket.x, bucket.y, bucket.width, bucket.height);

        for (Rectangle raindrop : raindrops) {
            game.batch.draw(dropImage, raindrop.x, raindrop.y);

        }

        for (Rectangle raindrop : redRainDrops) {
            game.batch.draw(dropImageRed, raindrop.x, raindrop.y);
        }

        game.batch.end();
        // process user input
        if (Gdx.input.isTouched()) {
            Vector3 touchPos = new Vector3();
            touchPos.set(Gdx.input.getX(), Gdx.input.getY(), 0);
            camera.unproject(touchPos);
            bucket.x = touchPos.x - 64 / 2;
        }
        if (Gdx.input.isKeyPressed(Input.Keys.LEFT))
            bucket.x -= 200 * Gdx.graphics.getDeltaTime();
        if (Gdx.input.isKeyPressed(Input.Keys.RIGHT))
            bucket.x += 200 * Gdx.graphics.getDeltaTime();

        // make sure the bucket stays within the screen bounds
        if (bucket.x < 0)
            bucket.x = 0;
        if (bucket.x > 800 - 64)
            bucket.x = 800 - 64;

        // check if we need to create a new raindrop
        if (TimeUtils.nanoTime() - lastDropTime > 1000000000)
            spawnRaindrop();

        if (TimeUtils.millis() - lastRedDropTime > 10000) {
            spawnRaindropRed();
        }

        // move the raindrops, remove any that are beneath the bottom edge of
        // the screen or that hit the bucket. In the later case we increase the
        // value our drops counter and add a sound effect.
        Iterator<Rectangle> iter = raindrops.iterator();
        Iterator<Rectangle> iterRed = redRainDrops.iterator();
        while (iter.hasNext()) {
            Rectangle raindrop = iter.next();
            //Rectangle redrrain = iterRed.next();
            raindrop.y -= 200 * Gdx.graphics.getDeltaTime();
            // redrrain.y -= 200 * Gdx.graphics.getDeltaTime();
            if ( (raindrop.y + 64 < 0) )
                iter.remove();
            //iterRed.remove();
            if (raindrop.overlaps(bucket)) {
                dropsGathered++;
                dropSound.play();
                iter.remove();
            }
            if(raindrop.getY() < 0 ) {
                dropsGathered--;
                dropSound.play();
            }
        }

        Image image = new Image(dropImageRed);
        // red drops loop
        while (iterRed.hasNext()) {
            Rectangle raindrops = iterRed.next();
            raindrops.y -= 210 * Gdx.graphics.getDeltaTime();
            if ( (raindrops.y + 64 < 0) )
                iterRed.remove();
            if (raindrops.overlaps(bucket)) {
                dropsGathered--;
                iterRed.remove();
            }
        }

        if(dropsGathered == 10) {
            //game.setScreen(new Finish(game, dropsGathered));
        }

    }
    public Rectangle getRect() {
        // return the collision rectangle for checking overlaps
        return bottom;
    }

    @Override
    public void resize(int width, int height) {
    }

    @Override
    public void show() {
        // start the playback of the background music
        // when the screen is shown
        rainMusic.play();
    }

    @Override
    public void hide() {

    }

    @Override
    public void pause() {
    }

    @Override
    public void resume() {
    }


    @Override
    public void dispose() {
        dropImage.dispose();
        dropImageRed.dispose();
        bucketImage.dispose();
        dropSound.dispose();
        rainMusic.dispose();
    }


}
