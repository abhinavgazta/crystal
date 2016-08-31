package com.mygdx.game;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Screen;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.GL20;
import com.badlogic.gdx.graphics.OrthographicCamera;

/**
 * Created by abhinavgazta on 8/13/16.
 */
public class LevelTwoMenu implements Screen {

    final DropLevelTwo game;
    OrthographicCamera camera;


    public LevelTwoMenu(final DropLevelTwo gam) {
        game = gam;
        camera = new OrthographicCamera();
        camera.setToOrtho(false, 800, 480);
    }

    @Override
    public void show() {

    }

    @Override
    public void render(float delta) {
        Gdx.gl.glClearColor(0, 0, 0.2f, 1);
        Gdx.gl.glClear(GL20.GL_COLOR_BUFFER_BIT);

        camera.update();
        game.batch.setProjectionMatrix(camera.combined);
        game.batch.begin();
        game.font.draw(game.batch, "Welcome to level two!!! ", 300, 450, 250, 1, false);
        game.font.getData().setScale(2, 2);
        game.font.draw(game.batch, "Press anywhere to begin!", 260, 300, 300, 2, false);

        game.font.setOwnsTexture(true);
        game.font.setColor(Color.GOLD);
        game.batch.end();

        if (Gdx.input.isTouched()) {
            game.setScreen(new GameScreenLevelTwo(game));
            dispose();
        }
    }

    @Override
    public void resize(int width, int height) {

    }

    @Override
    public void pause() {

    }

    @Override
    public void resume() {

    }

    @Override
    public void hide() {

    }

    @Override
    public void dispose() {

    }


}
