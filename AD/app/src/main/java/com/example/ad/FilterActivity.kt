package com.example.ad

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.appcompat.app.ActionBar
import com.example.ad.databinding.ActivityFilterBinding

class FilterActivity : AppCompatActivity() {

    //ViewBinding
    private lateinit var binding: ActivityFilterBinding

    //ActionBar
    private lateinit var actionBar: ActionBar

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityFilterBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.ivCapture.setOnClickListener {
            startActivity(Intent(this, SignUpActivity::class.java))
        }

        binding.ivFilter.setOnClickListener {
            startActivity(Intent(this, SignUpActivity::class.java))
        }

    }
    private fun checkPermissionAndGive(){

    }
}